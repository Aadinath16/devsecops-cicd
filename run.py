from app import create_app

app = create_app()

# Secure Fix: Protect the server invocation loop
if __name__ == '__main__':
    app.run(debug=False) # Turned debug off for pipeline safety