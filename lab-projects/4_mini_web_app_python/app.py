"""Mini Web App: a simple notes / to-do list using only Python's standard library."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from html import escape

notes = []  # stored in memory (resets when server restarts)

PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Mini Notes App</title>
<style>
 body{{font-family:Arial;max-width:480px;margin:40px auto;padding:0 16px}}
 input[type=text]{{width:70%;padding:8px}} button{{padding:8px 12px}}
 li{{margin:8px 0}}
</style></head><body>
<h2>Mini Notes App</h2>
<form method="POST" action="/add">
  <input type="text" name="note" placeholder="Write a note..." required>
  <button>Add</button>
</form>
<ul>{items}</ul>
</body></html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        items = "".join(
            f'<li>{escape(n)} <a href="/delete?i={i}">[x]</a></li>' for i, n in enumerate(notes)
        )
        self.send_html(PAGE.format(items=items or "<li>No notes yet.</li>"))

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        data = parse_qs(self.rfile.read(length).decode())
        text = data.get("note", [""])[0].strip()
        if text:
            notes.append(text)
        self.redirect("/")

    def send_html(self, body):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode())

    def redirect(self, where):
        self.send_response(303)
        self.send_header("Location", where)
        self.end_headers()

    # delete handled via GET for simplicity
    def do_HEAD(self):
        self.send_response(200); self.end_headers()


_orig_get = Handler.do_GET


def do_get_with_delete(self):
    if self.path.startswith("/delete"):
        try:
            idx = int(self.path.split("i=")[1])
            notes.pop(idx)
        except (IndexError, ValueError):
            pass
        return self.redirect("/")
    return _orig_get(self)


Handler.do_GET = do_get_with_delete

if __name__ == "__main__":
    print("Running at http://localhost:8000  (Ctrl+C to stop)")
    HTTPServer(("localhost", 8000), Handler).serve_forever()
