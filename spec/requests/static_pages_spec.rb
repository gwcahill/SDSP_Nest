require 'spec_helper'

describe "StaticPages" do
  describe "Home page" do
    it "should have the content 'Smart Building Data Visualization'" do
      visit '/static_pages/home'
      expect(page).to have_content('Smart Building Data Visualization')
    end
  end
end
