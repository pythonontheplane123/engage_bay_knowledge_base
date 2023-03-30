import urllib.request

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import sys
import fileinput
from os.path import join

#html_page = urlopen(url)
#soup = BeautifulSoup(html_page, "lxml")

'''
ye = 0
req = Request("https://help.engagebay.com")
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

links = []
for link in soup.findAll('a'):
    print(ye)
    links.append(link.get('href'))
    ye += 1

links_layer_2 = []
for word in links:
    if 'collections' in word:

        links_layer_2.append('https://help.engagebay.com'+word)
'''

links_layer_2 = ['https://help.engagebay.com/collections/faqs', 'https://help.engagebay.com/collections/default-collection', 'https://help.engagebay.com/collections/marketing-module', 'https://help.engagebay.com/collections/service-module', 'https://help.engagebay.com/collections/live-chat', 'https://help.engagebay.com/collections/other-settings']

links_layer_3 = []

ye = 0
req = Request(links_layer_2[0])

def search_for_link(url):
    links = []
    html_page = urlopen(url)
    soup = BeautifulSoup(html_page, "lxml")

    for link in soup.findAll('a'):
        b = link.get('href')
        if 'article' in b:
            links.append('https://help.engagebay.com'+b)
    return links

#create a loop for getting all 200 article links and titles:
#remove the https: part and replace the '-' with spaces to make the title and then just add the text at the bottom of the title
"""
all_arr_links = []
progress = 0
for x in links_layer_2:
    to_append = search_for_link(x)
    print(progress)
    all_arr_links = all_arr_links+to_append
    progress +=1
"""
all_links_final = ['https://help.engagebay.com/articles/how-to-get-my-daily-email-limit-increased', 'https://help.engagebay.com/articles/replylto', 'https://help.engagebay.com/articles/replies', 'https://help.engagebay.com/articles/removing_address', 'https://help.engagebay.com/articles/remove_unsubscribelinks', 'https://help.engagebay.com/articles/brandedemails', 'https://help.engagebay.com/articles/remove_branding', 'https://help.engagebay.com/articles/what-are-hard-bounces-and-soft-bounces', 'https://help.engagebay.com/articles/nocontacts', 'https://help.engagebay.com/articles/how-to-send-a-follow-up-emails', 'https://help.engagebay.com/articles/how-to-update-address-in-the-footer-of-the-emails', 'https://help.engagebay.com/articles/why-does-my-completed-tasks-doesnt-appear', "https://help.engagebay.com/articles/why-does-embedded-youtube-video-on-landing-page-doesn't-work", "https://help.engagebay.com/articles/why-do-sequence-stats-doesn't-update-after-adding-the-contacts-to-the-sequence", 'https://help.engagebay.com/articles/email-broadcast-shows-i-have-reached-my-daily-limit.-why', 'https://help.engagebay.com/articles/emailvalidation', 'https://help.engagebay.com/articles/how-to-export-contacts', 'https://help.engagebay.com/articles/rcfromstaticlist', 'https://help.engagebay.com/articles/how-to-merge-contacts', 'https://help.engagebay.com/articles/how-do-i-find-hard-bounces---soft-bounces---spam-complaints---unsubscribed-contacts', 'https://help.engagebay.com/articles/where-can-i-find-my-invoices', 'https://help.engagebay.com/articles/how-to-remove-contacts-from-a-sequence', 'https://help.engagebay.com/articles/how-to-get-a-pdf-downloaded-after-the-form-is-submitted', 'https://help.engagebay.com/articles/how-to-remove-contacts-from-the-automation', 'https://help.engagebay.com/articles/how-to-remove-contacts-from-the-workflow', 'https://help.engagebay.com/articles/acl', 'https://help.engagebay.com/articles/deletefromemail', 'https://help.engagebay.com/articles/testemails', 'https://help.engagebay.com/articles/how-to-move-contacts-from-one-list-to-another-list', 'https://help.engagebay.com/articles/why-am-i-unable-to-add-a-user', 'https://help.engagebay.com/articles/landing_pages_on_mobile', 'https://help.engagebay.com/articles/how-to-create-a-list-of-100-contacts', 'https://help.engagebay.com/articles/how-to-export-deals', 'https://help.engagebay.com/articles/how-to-send-resubscribe-email', 'https://help.engagebay.com/articles/how-to-find-all-the-opens-from-an-email-broadcast-and-add-them-to-a-static-list', 'https://help.engagebay.com/articles/scheduler', 'https://help.engagebay.com/articles/opensnclicks', 'https://help.engagebay.com/articles/how-to-create-a-ticket-from-the-form-submission', 'https://help.engagebay.com/articles/chrome_extension', 'https://help.engagebay.com/articles/difference-between-smart-and-static-list', 'https://help.engagebay.com/articles/how-to-create-custom-fields', 'https://help.engagebay.com/articles/how-to-create-lists', 'https://help.engagebay.com/articles/how-to-add-products', 'https://help.engagebay.com/articles/how-to-create-or-import-companies', 'https://help.engagebay.com/articles/difference-between-automation-and-workflows', 'https://help.engagebay.com/articles/-how-to-add-deals', 'https://help.engagebay.com/articles/how-to-change-the-view-on-task-and-deals', 'https://help.engagebay.com/articles/how-to-create-custom-deal-tracks', 'https://help.engagebay.com/articles/how-to-filter-contacts', 'https://help.engagebay.com/articles/how-to-configure-the-calendar', 'https://help.engagebay.com/articles/how-do-i-customize-the-calendar-url-and-the-calendar-page', 'https://help.engagebay.com/articles/how-to-create-tasks', 'https://help.engagebay.com/articles/how-to-create-task-types-and-statuses', 'https://help.engagebay.com/articles/how-to-create-proposals', 'https://help.engagebay.com/articles/how-to-set-up-2-way-sync-with-your-email-account', 'https://help.engagebay.com/articles/how-do-i-generate-reports', 'https://help.engagebay.com/articles/how-do-you-create-automation-on-sales', 'https://help.engagebay.com/articles/where-can-i-customize-the-confirmation-email', 'https://help.engagebay.com/articles/how-to-create-or-import-contacts', 'https://help.engagebay.com/articles/how-can-i-create-slots', 'https://help.engagebay.com/articles/how-to-send-reminder-emails-for-appointments', 'https://help.engagebay.com/articles/how-to-perform-bulk-actions', 'https://help.engagebay.com/articles/how-do-you-create-workflows', 'https://help.engagebay.com/articles/how-to-filter-deals', 'https://help.engagebay.com/articles/how-to-create-a-sequence-on-the-sales-module', 'https://help.engagebay.com/articles/how-do-i-access-deleted-contacts-and-others', 'https://help.engagebay.com/articles/how-to-upload-my-files-that-can-be-attached-to-emails', 'https://help.engagebay.com/articles/what-is-lead-score', 'https://help.engagebay.com/articles/how-to-search-for-contacts', 'https://help.engagebay.com/articles/how-to-save-filters', 'https://help.engagebay.com/articles/how-do-i-use-the-saved-filters', 'https://help.engagebay.com/articles/-how-do-i-customize-the-columns-i-want-to-see-on-the-contacts-list', 'https://help.engagebay.com/articles/what-type-of-bulk-actions-can-i-perform,-and-how', 'https://help.engagebay.com/articles/how-do-i-sort-contacts', 'https://help.engagebay.com/articles/how-do-i-merge-contacts', 'https://help.engagebay.com/articles/how-many-types-of-custom-fields-can-i-create-and-use', 'https://help.engagebay.com/articles/how-do-i-duplicate-a-contact', 'https://help.engagebay.com/articles/-how-do-i-edit-a-contact', 'https://help.engagebay.com/articles/how-do-i-choose-the-fields-i-want-to-see-on-the-contact-form', 'https://help.engagebay.com/articles/how-do-i-customize-the-columns-i-can-see-on-deals', 'https://help.engagebay.com/articles/how-do-i-sort-deals', 'https://help.engagebay.com/articles/what-kind-of-bulk-actions-can-i-perform-on-deals', 'https://help.engagebay.com/articles/what-kind-of-automation-can-i-execute-on-the-sales-module', 'https://help.engagebay.com/articles/what-are-the-different-triggers-and-how-does-each-of-them-work', 'https://help.engagebay.com/articles/what-are-the-different-actions-and-conditions-under-the-crm--sales-tab-of-the-automation-builder', 'https://help.engagebay.com/articles/-explain-what-each-of-these-actions-and-conditions-does', 'https://help.engagebay.com/articles/what-are-activities-', 'https://help.engagebay.com/articles/how-do-i-see-users-activities-on-the-system', 'https://help.engagebay.com/articles/what-kind-of-custom-reports-can-we-generate', 'https://help.engagebay.com/articles/-how-do-we-access-the-reports', 'https://help.engagebay.com/articles/how-to-import-deals', 'https://help.engagebay.com/articles/creating-appointment-links', 'https://help.engagebay.com/articles/how-to-create-or-import-contacts-p6u1zxig', 'https://help.engagebay.com/articles/how-to-create-lists-bpyl3fmc', 'https://help.engagebay.com/articles/difference-between-smart-and-static-list-do5phvvw', 'https://help.engagebay.com/articles/how-to-create-forms', 'https://help.engagebay.com/articles/can-i-import-my-own-code-to-create-a-landing-page', 'https://help.engagebay.com/articles/difference-between-inline-and-pop-up-forms', 'https://help.engagebay.com/articles/how-do-i-add-the-form-to-the-website', 'https://help.engagebay.com/articles/how-to-build-landing-pages', 'https://help.engagebay.com/articles/how-do-i-customize-the-url-of-the-landing-page', 'https://help.engagebay.com/articles/how-do-i-add-a-form-to-the-landing-page', 'https://help.engagebay.com/articles/how-do-i-create-a-video-template', 'https://help.engagebay.com/articles/how-do-i-create-email-templates', 'https://help.engagebay.com/articles/can-i-import-my-own-code-to-create-a-template', 'https://help.engagebay.com/articles/how-can-i-see-contacts-that-submitted-a-form', 'https://help.engagebay.com/articles/how-do-i-use-the-email-or-video-templates-i-created', 'https://help.engagebay.com/articles/what-is-a-broadcast,-and-how-do-you-create-one', 'https://help.engagebay.com/articles/what-is-an-ab-broadcast-and-how-i-create-one', 'https://help.engagebay.com/articles/what-is-an-rss-broadcast-and-how-to-set-it-up', 'https://help.engagebay.com/articles/how-do-i-duplicate-a-broadcast', 'https://help.engagebay.com/articles/how-can-i-check-for-opens-and-other-stats', 'https://help.engagebay.com/articles/can-i-resend-the-email-to-the-ones-who-did-not-open-the-email', 'https://help.engagebay.com/articles/can-i-schedule-a-time-for-the-emails-to-be-sent-at', 'https://help.engagebay.com/articles/what-is-an-email-sequence', 'https://help.engagebay.com/articles/how-to-create-a-sequence', 'https://help.engagebay.com/articles/how-do-i-duplicate-a-sequence', 'https://help.engagebay.com/articles/how-do-i-check-the-stats-for-a-sequence', 'https://help.engagebay.com/articles/what-is-automation', 'https://help.engagebay.com/articles/what-is-a-workflow', 'https://help.engagebay.com/articles/difference-between-automation-and-workflows-mxtntdpn', 'https://help.engagebay.com/articles/what-are-the-different-triggers-you-can-use-on-an-automation', 'https://help.engagebay.com/articles/what-are-actions-and-conditions-and-how-to-use-them', 'https://help.engagebay.com/articles/how-to-run-an-sms-broadcast', 'https://help.engagebay.com/articles/how-do-i-add-my-social-media-accounts', 'https://help.engagebay.com/articles/how-to-schedule-posts-to-social-media', 'https://help.engagebay.com/articles/what-kind-of-reports-can-i-generate', 'https://help.engagebay.com/articles/how-to-add-reports-to-the-marketing-dashboard', 'https://help.engagebay.com/articles/what-are-sticky-bars', 'https://help.engagebay.com/articles/what-are-site-messages', 'https://help.engagebay.com/articles/what-is-a-web-rule', 'https://help.engagebay.com/articles/how-do-i-set-up-push-notifications', 'https://help.engagebay.com/articles/how-do-i-personalize-my-emails', 'https://help.engagebay.com/articles/can-i-send-emails-directly-to-a-contact', 'https://help.engagebay.com/articles/how-does-web-analytics-work-', 'https://help.engagebay.com/articles/what-is-custom-domain-', 'https://help.engagebay.com/articles/how-to-remove-a-contact-from-an-automation', 'https://help.engagebay.com/articles/what-are-the-different-options-on-forms', 'https://help.engagebay.com/articles/what-can-i-do-on-the-change-text-tab', 'https://help.engagebay.com/articles/what-is-look--feel', 'https://help.engagebay.com/articles/what-are-fields', 'https://help.engagebay.com/articles/-what-are-temporary-fields', 'https://help.engagebay.com/articles/what-are-hidden-fields-and-how-do-i-use-them', 'https://help.engagebay.com/articles/what-is-a-validation-pattern', 'https://help.engagebay.com/articles/what-are-the-different-options-on-the-settings-tab', 'https://help.engagebay.com/articles/what-is-style-on-popup-forms', 'https://help.engagebay.com/articles/what-is-call-to-action-on-popup-forms', 'https://help.engagebay.com/articles/what-are-the-different-options-on-the-settings-tab-of-the-popup-form', 'https://help.engagebay.com/articles/how-do-i-enable-recaptcha-for-my-forms', 'https://help.engagebay.com/articles/other-options-under-settings', 'https://help.engagebay.com/articles/what-are-the-different-types-of-content-i-can-use-on-landing-pages', 'https://help.engagebay.com/articles/-what-are-blocks-on-the-landing-page-builder', 'https://help.engagebay.com/articles/-can-i-save-a-block-and-reuse-it-on-another-page', 'https://help.engagebay.com/articles/what-are-views,-unique-views,-contact,-and-conversions', 'https://help.engagebay.com/articles/what-is-a-category-for-email-template', 'https://help.engagebay.com/articles/what-are-blocks-on-template-builder', 'https://help.engagebay.com/articles/what-are-the-different-types-of-content-i-can-use-on-templates', 'https://help.engagebay.com/articles/what-is-select-filter-on-broadcasts', 'https://help.engagebay.com/articles/-what-do-i-exclude-lists-from-a-sequence', 'https://help.engagebay.com/articles/can-i-change-the-order-of-emails-on-the-sequence', 'https://help.engagebay.com/articles/what-are-the-different-triggers-for-marketing-automation-and-how-do-they-each-work', 'https://help.engagebay.com/articles/what-are-the-different-actions-and-conditions-on-the-contact-tab-of-the-automation-builder-', 'https://help.engagebay.com/articles/what-are-activities-under-marketing', 'https://help.engagebay.com/articles/what-kind-of-reports-can-be-generated-under-marketing', 'https://help.engagebay.com/articles/how-do-i-access-the-reports', 'https://help.engagebay.com/articles/how-to-add-tags', 'https://help.engagebay.com/articles/how-to-add-contacts-to-the-sequence', 'https://help.engagebay.com/articles/how-to-set-up-the-service-module', 'https://help.engagebay.com/articles/how-to-create-a-support-group', 'https://help.engagebay.com/articles/how-do-i-receive-tickets-on-the-service-module', 'https://help.engagebay.com/articles/how-do-i-choose-who-the-ticket-is-assigned-to', 'https://help.engagebay.com/articles/how-do-i-assign-the-ticket-to-another-user', 'https://help.engagebay.com/articles/how-to-change-the-ticket-priority-or-type', 'https://help.engagebay.com/articles/views', 'https://help.engagebay.com/articles/how-to-set-up-automation-on-the-service-module', 'https://help.engagebay.com/articles/what-would-each-of-the-triggers-on-service-automation-allow', 'https://help.engagebay.com/articles/what-is-a-macro-and-how-is-it-different-from-automation', 'https://help.engagebay.com/articles/how-do-i-execute-a-macro', 'https://help.engagebay.com/articles/-what-are-canned-responses', 'https://help.engagebay.com/articles/how-do-i-use-a-canned-response', 'https://help.engagebay.com/articles/-how-do-i-add-more-ticket-types,-statuses,-and-priorities', 'https://help.engagebay.com/articles/knowledgebase', 'https://help.engagebay.com/articles/addarticles', 'https://help.engagebay.com/articles/how-do-i-publish-the-articles', 'https://help.engagebay.com/articles/what-is-a-collection', 'https://help.engagebay.com/articles/customizelooknfeel', 'https://help.engagebay.com/articles/customizeurl', 'https://help.engagebay.com/articles/how-do-i-enable-the-chat-widget', 'https://help.engagebay.com/articles/where-do-i-receive-the-chat-and-how-can-i-answer-them', 'https://help.engagebay.com/articles/can-i-receive-notifications-when-a-new-chat-is-received', 'https://help.engagebay.com/articles/what-details-can-i-ask-for-before-someone-initiates-a-chat', 'https://help.engagebay.com/articles/can-i-customize-the-chat-widget', 'https://help.engagebay.com/articles/can-i-disable-the-chat-during-non-business-hours', 'https://help.engagebay.com/articles/how-can-i-define-my-business-hours', 'https://help.engagebay.com/articles/can-i-send-an-email-with-the-transcript-once-the-chat-ends', 'https://help.engagebay.com/articles/what-are-shortcuts-and-how-do-i-use-them', 'https://help.engagebay.com/articles/can-i-show-the-chat-widget-when-someone-clicks-on-a-button-on-the-website', 'https://help.engagebay.com/articles/how-to-enable-chatbot', 'https://help.engagebay.com/articles/how-to-sync-data', 'https://help.engagebay.com/articles/integrating-whatsapp', 'https://help.engagebay.com/articles/how-to-delete-the-account', 'https://help.engagebay.com/articles/how-to-set-up-telephony-integration', 'https://help.engagebay.com/articles/enable-the-chat-widget', 'https://help.engagebay.com/articles/how-do-i-integrate-my-zoom-account', 'https://help.engagebay.com/articles/what-is-a-smart-bcc', 'https://help.engagebay.com/articles/docusign_integration', 'https://help.engagebay.com/articles/-how-to-add-an-email-signature', 'https://help.engagebay.com/articles/how-to-integrate-google-outlook-office-365-calendars', 'https://help.engagebay.com/articles/authenticate-domain', 'https://help.engagebay.com/articles/what-is-vanity-url-and-how-to-set-it-up', 'https://help.engagebay.com/articles/integration-with-zero-bounce--validating-the-contacts', 'https://help.engagebay.com/articles/how-do-i-enable-hubspot-sync']

path = '/Users/macos/desktop/ze_knowledge_base'

for index in range(203):
    soup = BeautifulSoup(urlopen(all_links_final[index].replace('&#39;',"'").replace('doesnt',"doesn't")),'lxml')
    result = soup.find("div", {"class": "article-body"})
    TEXT = result.text
    TEXT = TEXT.replace('<br>', '').replace('&nbsp;', '').replace(' ', '').replace('/n','').replace('&#39;',"'")
    filename = all_links_final[index].replace('https://help.engagebay.com/articles/', '').replace('-',' ')

    with open(join(path,filename+'.txt'), 'w') as file:
        file.write(all_links_final[index].replace('https://help.engagebay.com/articles/', '')+'.'+ TEXT)
    print(index)


for index in range(203,len(all_links_final)):
    soup = BeautifulSoup(urlopen(all_links_final[index].replace('&#39;',"'").replace('doesnt',"doesn't")),'lxml')
    result = soup.find("div", {"class": "article-body"})
    TEXT = result.text
    TEXT = TEXT.replace('<br>', '').replace('&nbsp;', '').replace(' ', '').replace('/n','').replace('&#39;',"'")
    filename = all_links_final[index].replace('https://help.engagebay.com/articles/', '').replace('-',' ')

    with open(join(path,filename+'.txt'), 'w') as file:
        file.write(all_links_final[index].replace('https://help.engagebay.com/articles/', '')+'.'+ TEXT)
    print(index)

soup = BeautifulSoup(urlopen('https://help.engagebay.com/articles/how-do-i-enable-the-chat-widget'.replace('&#39;',"'").replace('doesnt',"doesn't")),'lxml')
result = soup.find("div", {"class": "article-body"})
TEXT = result.text
TEXT = TEXT.replace('<br>', '').replace('&nbsp;', '').replace(' ', '').replace('/n','').replace('&#39;',"'")
filename = 'https://help.engagebay.com/articles/how-do-i-enable-the-chat-widget'.replace('https://help.engagebay.com/articles/', '').replace('-',' ')

with open(join(path,filename+'.txt'), 'w') as file:
    file.write('https://help.engagebay.com/articles/how-do-i-enable-the-chat-widget'.replace('https://help.engagebay.com/articles/', '')+'.'+ TEXT)

"""
arr = []

for index in range(203):
    try:
        soup = BeautifulSoup(urlopen(all_links_final[index].replace('&#39;',"'").replace('doesnt',"doesn't")),'lxml')
        result = soup.find("div", {"class": "article-body"})
        TEXT = result.text
        TEXT = TEXT.replace('<br>', '').replace('&nbsp;', '').replace(' ', '').replace('/n','').replace('&#39;',"'")
        filename = all_links_final[index].replace('https://help.engagebay.com/articles/', '').replace('-',' ')

        arr.append(all_links_final[index].replace('https://help.engagebay.com/articles/', '')+'.'+ TEXT)
        print(index)
    except:
        continue


for index in range(203,len(all_links_final)):
    try:
        soup = BeautifulSoup(urlopen(all_links_final[index].replace('&#39;',"'").replace('doesnt',"doesn't")),'lxml')
        result = soup.find("div", {"class": "article-body"})
        TEXT = result.text
        TEXT = TEXT.replace('<br>', '').replace('&nbsp;', '').replace(' ', '').replace('/n','').replace('&#39;',"'")
        filename = all_links_final[index].replace('https://help.engagebay.com/articles/', '').replace('-',' ')

        arr.append(all_links_final[index].replace('https://help.engagebay.com/articles/', '')+'.'+ TEXT)
        print(index)
    except:
        continue

soup = BeautifulSoup(urlopen('https://help.engagebay.com/articles/how-do-i-enable-the-chat-widget'.replace('&#39;',"'").replace('doesnt',"doesn't")),'lxml')
result = soup.find("div", {"class": "article-body"})
TEXT = result.text
TEXT = TEXT.replace('<br>', '').replace('&nbsp;', '').replace(' ', '').replace('/n','').replace('&#39;',"'")
filename = 'https://help.engagebay.com/articles/how-do-i-enable-the-chat-widget'.replace('https://help.engagebay.com/articles/', '').replace('-',' ')
arr.append('https://help.engagebay.com/articles/how-do-i-enable-the-chat-widget'.replace('https://help.engagebay.com/articles/', '')+'.'+ TEXT)
print(arr)
"""
#copy paste all the content inside the tags of div class = 'article-body' and replace the weird n thing with spaces

