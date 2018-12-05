"""

The main models for ORM (Object Relationship Manager).
"""

from app import db


class EquityData(db.Model):
    """

    Define the table EquityData containing time series data for equities.
    """
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(64), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    open = db.Column(db.Integer, nullable=False)
    high = db.Column(db.Integer, nullable=False)
    low = db.Column(db.Integer, nullable=False)
    close = db.Column(db.Integer, nullable=False)
    volume = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """

        Print objects of class EquityData.
        :return: string
        """
        return '<Ticker {}, Date {}, Open {}, High {}, Low {}, Close {}, Volume {}>'\
            .format(self.ticker, self.date, self.open, self.high, self.low, self.close, self.volume)
