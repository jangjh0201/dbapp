if __name__ == "__main__":
    import uvicorn
    from app.dbapp import DBApp

    db_app = DBApp()
    app = db_app.get_app()

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
