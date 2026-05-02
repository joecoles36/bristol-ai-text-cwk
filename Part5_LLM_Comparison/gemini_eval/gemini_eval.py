from google import genai
from PIL import Image
import os
import pandas as pd
from datetime import datetime
from prompts import *

client = genai.Client()

def run_eval(image_folder, prompt, output_file):
    results = []

    for file in sorted(os.listdir(image_folder)):
        if not file.endswith(".png"):
            continue

        path = os.path.join(image_folder, file)
        img = Image.open(path)

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, img]
            )

            text = response.text

        except Exception as e:
            text = f"ERROR: {str(e)}"

        results.append({
            "image_id": file,
            "prompt": prompt,
            "response": text,
            "timestamp": datetime.now()
        })

        print(f"Done {file}")

    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)


# RUN
if __name__ == "__main__":
    run_eval("../images/numbers", NUMBERS_PROMPT, "numbers_responses.csv")
    run_eval("../images/tictactoe", TICTACTOE_PROMPT, "tictactoe_responses.csv")
    run_eval("../images/shapes", SHAPES_PROMPT, "shapes_responses.csv")
