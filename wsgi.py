from app import application
import os

if __name__ == "__main__":
    # ON_HEROKU will be 1 if True
    ON_HEROKU = os.environ.get('ON_HEROKU', None)

    if ON_HEROKU == 1:
        print("Running on Heroku...")
        port = int(os.environ.get('PORT', 17995))
        
    else:
        print("Running on local...")
        port = 8000
        
    application.run(host='0.0.0.0', port=port)