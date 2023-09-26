import sys
from lms_application import LMSApplication

def main():
    app = LMSApplication()
    app.execute(sys.argv[1])

if __name__ == "__main__":
    main()
