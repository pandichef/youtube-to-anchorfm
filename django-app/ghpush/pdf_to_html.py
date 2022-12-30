import os
import re
import requests


def download_pdf_file(url):
    assert url.endswith('.pdf'), 'URL must point to a PDF file'
    filename = url.split('/')[-1]
    docname = filename.split('.')[0]

    # os.system('rm -rf output')
    # os.mkdir('output')
    # os.mkdir('output/' + docname)

    # Download the PDF file
    response = requests.get(url)

    # Save the content to a local PDF file
    with open('deleteme.pdf', 'wb') as f:
        f.write(response.content)

    return docname


def convert_pdf_to_html(docname):
    # using pdftohtml (linux command line tool)
    os.system('rm -rf static/pdf_to_html/' + docname)
    try:
        os.mkdir('static/pdf_to_html/' + docname)
    except FileNotFoundError:
        os.mkdir('static/pdf_to_html')
        os.mkdir('static/pdf_to_html/' + docname)
    # os.system('pdftohtml -c -noframes -s -nomerge ' + 'deleteme.pdf ' +
    # os.system('pdftohtml -noframes -s ' + 'deleteme.pdf ' +
    os.system('pdftohtml -noframes -s ' + 'deleteme.pdf ' +
              'static/pdf_to_html/' + docname + '/index.html')
    # os.system('rm output/' + docname + '/deleteme.pdf')
    os.system('rm deleteme.pdf')
    # replace every <br/> with space in index.html
    with open('static/pdf_to_html/' + docname + '/index.html', 'r') as f:
        html = f.read()
        html = html.replace('<br/>', ' ')
        # remove timestamps like 01-00:33:49; for d. valentine berkeley interview
        if docname == "valentine_donald":
            html = re.sub('\d{2}-\d{2}:\d{2}:\d{2}\s', '', html)
    os.system('rm static/pdf_to_html/' + docname + '/index.html')
    with open('static/pdf_to_html/' + docname + '/index.html', 'w') as f:
        f.write(html)


if __name__ == "__main__":
    os.chdir('..')
    url = 'https://digitalassets.lib.berkeley.edu/roho/ucb/text/valentine_donald.pdf'
    docname = download_pdf_file(url)
    convert_pdf_to_html(docname)
