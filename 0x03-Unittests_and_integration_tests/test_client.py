#!/usr/bin/env python3
"""Unit and integration tests for GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url method"""
        mock_org.return_value = {"repos_url": "http://test.com"}
        client = GithubOrgClient("test")
        self.assertEqual(client._public_repos_url, "http://test.com")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test public_repos method"""
        mock_repos_url.return_value = "http://test.com"
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        client = GithubOrgClient("test")
        repos = client.public_repos()
        self.assertEqual(repos, ["repo1", "repo2"])
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://test.com")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        self.assertEqual(GithubOrgClient.has_license(repo, license_key), expected)

