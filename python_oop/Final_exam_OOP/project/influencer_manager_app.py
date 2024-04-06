from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPES = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_TYPES_OF_CAMPIGNES = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}
    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []



    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        #influencer = [i for i in self.influencers if i.username == username][0]
        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."
        elif username in self.influencers:
            return f"{username} is already registered."
        else:
            influencer = self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."


    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_TYPES_OF_CAMPIGNES:
            return f"{campaign_type} is not a valid campaign type."
        elif campaign_id in self.campaigns:
            return f"Campaign ID {campaign_id} has already been created."
        else:
            campaign = self.VALID_TYPES_OF_CAMPIGNES[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."


    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = [i for i in self.influencers if i.username == influencer_username][0]
        except IndexError:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = [c for c in self.campaigns if c.campaign_id == campaign_id][0]
        except IndexError:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        if influencer.calculate_payment() > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment()
            influencer.campaign_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."


    def calculate_total_reached_followers(self):
        total_followers = 0
        for i in self.influencers:
            total_followers += i.reached_followers()


    def influencer_campaign_report(self, username: str):
        try:
            influencer = [i for i in self.influencers if i.username == username][0]
        except IndexError:
            return f"{username} has not participated in any campaigns."

        result = influencer.display_campaigns_participated()
        return result

    def campaign_statistics(self):
        pass






