from flask import Blueprint, render_template, redirect, request, flash, session
#from ..config.database import get_connection
from werkzeug.security import generate_password_hash, check_password_hash
#from ..utils.decorators import autheticated_admin, guest_admin, prevent_multiple
#from ..store.category import get_all_categories

admin = Blueprint("admin", __name__)
#db = get_connection()

@admin.get("/")
#@guest_admin # don,t understand
def login_page():
    return render_template("admin/login.html")