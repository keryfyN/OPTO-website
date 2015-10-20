import os
from application import create_app

# run the application!
if __name__ == '__main__':
     # Bind to PORT if defined, otherwise default to 5000.
     port = int(os.environ.get('PORT', 5000))
     app = create_app()
     app.run()
