import asyncio
from unittest.mock import patch, MagicMock
from app.config.database import init_db, get_database, close_db

def  test_init_db_connects_successfully():
    """Test that init_db successfully connects to MongoDB"""

    with patch('app.config.database.AsyncIOMotorClient') as mock_client:
        mock_db = MagicMock()
        mock_client.return_value.__getitem__.return_value = mock_db
        asyncio.run(init_db())
        mock_client.assert_called_once()


def  test_get_database_returns_db_instance():
    """test_get_database_returns_db_instance"""

    with patch('app.config.database.db') as mock_db:
        mock_db.name = 'feedback_db'
        
        database = asyncio.run(get_database())
        assert database is not None
        assert database.name == 'feedback_db'


def test_close_db_closes_connection():
    """Test that close_db properly closes MongoDB connection"""

    with patch('app.config.database.client') as mock_client:
        asyncio.run(close_db())
        mock_client.close.assert_called_once()