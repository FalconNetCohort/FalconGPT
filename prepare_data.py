import json

def txt_to_jsonl(file_path):
    with open(file_path, 'r') as f:
        paragraphs = [para for para in f.read().split("\n") if para.strip()]

    with open('CSD.jsonl', 'w') as outfile:
        for para in paragraphs:
            messages = [
                {"role": "system", "content": "You are an assistant trained on the CADET STANDARDS AND DUTIES document."},
                {"role": "user", "content": "Tell me about this section:"},
                {"role": "assistant", "content": para}
            ]

            json.dump({"messages": messages}, outfile)
            outfile.write('\n')

file_path = "./CSD.txt"
txt_to_jsonl(file_path)
