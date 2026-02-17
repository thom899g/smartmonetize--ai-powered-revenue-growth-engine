import logging
from typing import Dict, Optional
import requests
from bs4 import BeautifulSoup

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='data_collection.log'
)

class DataCollector:
    """Handles web scraping and API data collection for user behavior and market trends."""
    
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.121 Safari/537.36'
        }
        
    def collect_user_behavior(self, url: str) -> Dict:
        """Scrapes user interaction data from a given URL."""
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract user behavior metrics
            metrics = {
                'user_interactions': self._parse_user_actions(soup),
                'session_duration': self._extract_session_time(soup),
                'conversion_rate': self._calculate_conversion_rate(soup)
            }
            return metrics
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            raise
        
    def collect_market_trends(self, endpoint: str) -> Dict:
        """Fetches market trend data from an API endpoint."""
        try:
            response = requests.get(endpoint, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {e}")
            raise
    
    def _parse_user_actions(self, soup: BeautifulSoup) -> int:
        """Parses user action count from the webpage."""
        actions = soup.find_all('div', class_='user-action')
        return len(actions)
    
    def _extract_session_time(self, soup: BeautifulSoup) -> Optional[float]:
        """Extracts session duration in seconds."""
        time_tag = soup.find('span', class_='session-time')
        if time_tag:
            return float(time_tag.text)
        return None
    
    def _calculate_conversion_rate(self, soup: BeautifulSoup) -> float:
        """Calculates conversion rate based on form submissions."""
        conversion_elements = soup.find_all('div', class_='conversion')
        successful = sum(1 for el in conversion_elements if 'success' in el.text)
        total = len(conversion_elements)
        return (successful / total) * 100 if total > 0 else 0.0