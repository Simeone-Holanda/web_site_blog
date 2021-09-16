from website import create_app

#8 min

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)