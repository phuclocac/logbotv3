from app import app

# Export the app for Vercel
application = app

# For local development
if __name__ == "__main__":
    app.run(debug=True)