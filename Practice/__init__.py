# import cx_Oracle
# import sys
# import os
#
# try:
#     if sys.platform.startswith("darwin"):
#         lib_dir = os.path.join(os.environ.get("HOME"), "Downloads",
#                                "instantclient_19_8")
#         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
#     elif sys.platform.startswith("win32"):
#         lib_dir = r"$HOME/Downloads/instantclient_19_8"
#         cx_Oracle.init_oracle_client(lib_dir=lib_dir)
# except Exception as err:
#     print("Whoops!")
#     print(err);
#     sys.exit(1);
