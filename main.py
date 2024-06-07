from router import app

if __name__ == "__main__":
    import uvicorn
    print("Server is running...")
    uvicorn.run(app, host="0.0.0.0", port=9000)
