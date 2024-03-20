from flask import Flask, render_template
#from .config.variables import SECRET_KEY

def create_app():
    app = Flask(__name__)

    # CONFIGS
    #app.config["SECRET_KEY"] = SECRET_KEY

    # BLUEPRINTS
    from .views.admin_auth import admin
    app.register_blueprint(admin, url_prefix = "/")

    #from .views.category import category
    #app.register_blueprint(category, url_prefix="/owner")

    # ERROR ROUTES

    # 404 - ERROR
    # @app.errorhandler(404)
    # def page_not_found(error):
    #     return render_template("admin/error-404.html")
    # # 500 - ERROR
    # @app.errorhandler(500)
    # def internal_sever_error(error):
    #     return render_template("admin/error-404.html")
    
    
    return app