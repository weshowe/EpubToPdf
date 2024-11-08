import weasyprint
import os
from PyPDF2 import PdfFileMerger
from PyPDF2.utils import PdfReadError
import shutil
import tempfile

class PdfEngine(object):

    """
        This class carries operations on pdf files.

        It has the following methods:

        convert() --- Which converts each of the markup file
        passed in to pdf. Markup file should be html

        combine() --- Which merges all of the pdf files created by
        the convert method, creating a new file.

        del_pdf() --- Which deletes all the pdf files created by
        the convert method.

    """

    def __init__(self, markup_files, style_files, pdf_files, directory):
        self.markup_files = markup_files
        self.style_files = style_files
        self.pdf_files = pdf_files
        self.directory = directory
        self.tempdir = tempfile.mkdtemp()

    def convert(self):
        for each in self.markup_files:
            # Prevent conversion process from showing terminal updates
            #options = {"enable-local-file-access": None, "quiet": ""}
            #pdfkit.from_file(each, "{}.pdf".format(self.markup_files.index(each)),options=options)
            pdf = weasyprint.HTML(filename=each, encoding="utf-8")
            pdf.write_pdf(target=os.path.join(self.tempdir,"{}.pdf".format(self.markup_files.index(each))))

        print('--- Sections converted to pdf')

    def combine(self):

        merger = PdfFileMerger()

        for pdf in self.pdf_files:
            try:
                merger.append(os.path.join(self.tempdir,pdf), import_bookmarks=False)
            except PdfReadError:
                pass

        merger.write("{}.pdf".format(self.directory))

        print('--- Sections combined together in a single pdf file')

        merger.close()

    def del_pdf(self):
            shutil.rmtree(self.tempdir)
            print('--- Temporary pdf files deleted')
