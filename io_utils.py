import csv, json

def save_csv(data, filename):
    with open(filename,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["word","count"])
        for row in data:
            w.writerow(row)

def save_json(data, filename):
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

def save_md(data, filename):
    with open(filename,"w",encoding="utf-8") as f:
        f.write("| Word | Count |\n|---|---|\n")
        for w,c in data:
            f.write(f"| {w} | {c} |\n")

def save_html(data, filename):
    with open(filename,"w",encoding="utf-8") as f:
        f.write("<table border=1><tr><th>Word</th><th>Count</th></tr>")
        for w,c in data:
            f.write(f"<tr><td>{w}</td><td>{c}</td></tr>")
        f.write("</table>")
