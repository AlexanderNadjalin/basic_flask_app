from app import app, db
from app.models import EquityData


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'equity_data': EquityData}
