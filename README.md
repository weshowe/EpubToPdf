Originally by HAKSOAT (https://github.com/HAKSOAT/EpubToPdf). As a proud .epub hater, I made some improvements:

1) Changed from pdfkit to weasyprint as pdfkit wasn't rendering images and had crappy font formatting.
2) Added code to remove anchors as these won't work in PDF and they end up looking weird.
3) Don't destroy the input file during creation as we'll lose it if the program fails.
4) Put all the temp PDFs in a temp directory so you dont see a bazillion pdfs showing up in your CWD.
5) Support for relative paths in the input.
6) Updated BS4 dependency as it doesn't like newer Python versions.

So far I have tested this on 1 book. It ended up looking pretty nice, but if your PDF book ends up sucking feel free to let me know. Also you get what you pay for. :)

(Mostly) Original Readme:

# EpubToPdf

This program converts epub documents to pdf documents.


**Installation**

Clone this repository to your machine.


**Requirements**

To install the requirements, run the following command:

```pip install -r requirements.txt```

After this, you install weasyprint. Instructions here: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html. If you have Windows, you should be able to get by by just pip installing all the stuff. I didn't bother with the venv stuff because real programmers pack their default Python environment full of crap and pray for no dependency hell.

**Usage**

Copy the epub file inside the repository folder when forked.

Run the main.py file, adding the name of the epub file as a commandline argument.

As shown below:

```python main.py epub-file-name```
