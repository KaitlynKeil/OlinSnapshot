import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Note that with this setting, anyone on the local network can access your
    # development server. Probably not an issue on the Olin network; you might
    # want to conditionalize this value for host if you're spending much time
    # developing in caffes.
    app.run(host='0.0.0.0', port=port, debug=True)
