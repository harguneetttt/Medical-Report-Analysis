import os
import io
import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from PIL import Image
import easyocr
import google.generativeai as genai
from pydantic import BaseModel

conversation_context = {
    "report_text": "",
    "chat_history": []
}

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    with open("static/index.html", "r") as f:
        return f.read()


class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_with_gemini(req: ChatRequest):
    try:
        user_message = req.message

        conversation_context["chat_history"].append({"role": "user", "content": user_message})

        model = genai.GenerativeModel("gemini-2.5-flash")

        full_prompt = f"""
        You are an assistant that answers questions about medical reports.
        
        Here is the medical report text extracted from the uploaded image:
        --- REPORT START ---
        {conversation_context['report_text']}
        --- REPORT END ---

        Conversation so far:
        {conversation_context['chat_history']}

        User's new question:
        {user_message}

        Your job:
        - Answer based only on the report & general medical knowledge.
        - Explain clearly in simple terms.
        - Do NOT give medical advice or treatment instructions.
        """

        response = model.generate_content(full_prompt)

        bot_reply = response.text.replace("**", "")
        
        conversation_context["chat_history"].append({"role": "assistant", "content": bot_reply})

        return Response(content=bot_reply, media_type="text/plain")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")

reader = easyocr.Reader(['en'], gpu=False)

@app.post("/analyze-report")
async def analyze_report(file: UploadFile = File(...)):
    try:
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Upload an image file (PNG/JPG).")

        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        image_np = np.array(image)

        print(f"Incoming file: {file.filename}, size: {len(image_bytes)} bytes")

        print("Running OCR...")
        result = reader.readtext(image_np)
        extracted_text = " ".join([r[1] for r in result])

        if not extracted_text.strip():
            raise HTTPException(status_code=400, detail="No readable text found in image.")

        print("Extracted text length:", len(extracted_text))

        truncated_text = extracted_text[:1000]

        conversation_context["report_text"] = truncated_text
        conversation_context["chat_history"] = []

        print("Sending text to Gemini...")
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
        You are a medical report summarizer.
        Read this text and extract:
        - Summary of report
        - Abnormal findings
        - Prescribed medicines (if any)
        - Recommendations
        
        Text: {truncated_text}
        """

        response = model.generate_content(prompt)
        print("Response received from Gemini.")
        
        clean = response.text.replace("**", "")
        return HTMLResponse(clean.replace("\n", "<br>"))

    except Exception as e:
        print("Error:", str(e))
        raise HTTPException(status_code=500, detail=f"Error analyzing report: {str(e)}")
