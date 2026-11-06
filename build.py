#!/usr/bin/env python3
"""Build slides.html from slides.md using reveal.js's Markdown plugin.

Usage: python3 build.py [input.md] [output.html]

The Markdown is embedded in the HTML inside a <textarea data-template>,
and reveal.js converts it to slides in the browser, so the output is a
single static file that also works when opened straight from disk.
Only the Python standard library is needed.
"""

import sys
from pathlib import Path

TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tech Change at Work Talk</title>
  <link rel="stylesheet" href="reveal.js-master/dist/reveal.css">
  <link rel="stylesheet" href="reveal.js-master/dist/theme/white.css">
  <style>
    .reveal h1 { font-size: 2.2em; }
    .reveal h2 { font-size: 1.8em; }
    .reveal ul, .reveal ol {
      display: block;
      margin-left: 2em;
      text-align: left;
    }
    .reveal pre {
      margin: 1em auto;
      width: 90%;
      text-align: left;
    }
    .reveal blockquote {
      width: 90%;
      margin: 1em auto;
      text-align: left;
      font-style: italic;
      background: rgba(0,0,0,0.05);
      padding: 0.5em 1em;
      border-left: 5px solid rgba(0,0,0,0.1);
    }
    .reveal section {
      text-align: left;
    }
    .reveal .title-slide {
      text-align: center;
    }
  </style>
</head>
<body>
  <!-- GENERATED FILE: edit slides.md and run build.py instead. -->
  <div class="reveal">
    <div class="slides">
      <section data-markdown data-separator="^\\r?\\n---\\r?\\n$">
        <textarea data-template>
@@SLIDES@@
        </textarea>
      </section>
    </div>
  </div>

  <script src="reveal.js-master/dist/reveal.js"></script>
  <script src="reveal.js-master/plugin/markdown/markdown.js"></script>
  <script>
    Reveal.initialize({
      controls: true,
      progress: true,
      center: false,
      hash: true,
      transition: 'slide',
      plugins: [ RevealMarkdown ]
    });
  </script>
</body>
</html>
"""


def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else "slides.md")
    dst = Path(sys.argv[2] if len(sys.argv) > 2 else "slides.html")

    md = src.read_text(encoding="utf-8")

    # A literal </textarea> in the Markdown would end the textarea early.
    md = md.replace("</textarea>", "&lt;/textarea>")

    dst.write_text(TEMPLATE.replace("@@SLIDES@@", md.strip("\n")),
                   encoding="utf-8")
    print(f"wrote {dst} ({md.count(chr(10) + '---' + chr(10)) + 1} slides)")


if __name__ == "__main__":
    main()
