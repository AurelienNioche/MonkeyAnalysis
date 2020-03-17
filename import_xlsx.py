import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "MonkeyAnalysis.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from experimental_data.import_export import import_data_xlsx, \
    import_stimuli_xlsx


if __name__ == "__main__":

    # # For reproduction:
    # import_xls('data_GH.xlsx')
    import_data_xlsx()