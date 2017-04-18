import clearbit

clearbit.key = '1234567890'


emails = [
    u'britton.halle+tommyshark@gmail.com',
    u'rose.g123@hotmail.com',
    u'alex@tradecrafted.com',
    u'fahad@nogorweb.com',
    u'terrillo@gurustu.co',
    u'carla@computent.nl',
    u'leor@dormroommovers.com',
    u'mithomson@hotmail.com',
    u'aravind@notiphi.com',
    u'dukedave@gmail.com',
    u'erin@hotmamafit.com',
    u'terrillo@terrillo.me',
    u'urielx2@gmail.com',
    u'jeremy@onboardiq.com',
    u'keith@onboardiq.com',
    u'brenda.davis@sunrunhome.com',
    u'mirco@external.lottoland.com',
    u'orcc_12@yahoo.com',
    u'dan.bonville@finalsite.com']

results = {}

for email in emails:
    response = clearbit.PersonCompany.find(email=email, stream=True)
    results[email] = response

    # if 'person' in response:
    #     # deal with person
    #     print "found person for %s" % email
    #
    # if 'company' in response:
    #     # deal with company
    #     print "found company for %s" % email


def print_company(company):
    if not company:
        return

    if company['emailProvider']:
        return

    print "\n\t > Company: %s" % company.get('name', '')
    print "\t\t %s" % company.get('site', {}).get('url', '')

    print "\t Location: \n\t\t %s" % company.get('location', '')

    print "\t Metrics:"
    print_not_null(company.get('metrics', {}), depth=2)


def print_person(person):
    if not person:
        return

    print "\n\t > Person: %s" % person['email']
    print "\t\t Title: %s" % person['employment']['title']
    print "\t\t Name: %s" % person['name']['fullName']
    print "\t\t Bio: %s" % person['bio']


def print_not_null(o, depth=1):
    if type(o) == dict:
        for k, v in o.iteritems():
            if type(v) == dict:
                print "%s %s" % ('\t' * depth, k)
                print_not_null(v, depth=depth+1)
            elif v is not None:
                print "%s %s: %s" % ('\t' * depth, k, v)
    else:
        print o


for k, v in results.iteritems():
    print "New Lead: %s" % k
    print_person(v['person'])
    print_company(v['company'])


# def scoring(person, company):
#     defaults = {
#         twitter_followers_weight:   0.09,
#         angellist_followers_weight: 0.05,
#         klout_score_weight:         0.05,
#         company_twitter_followers_weight: 0.05,
#         company_alexa_rank_weight:  0.000005,
#         company_google_rank_weight: 0.05,
#         company_employees_weight:   0.5,
#         company_raised_weight:      0.00005,
#         company_score:              10,
#         total_score:                1415
#     }
#
#       def calculate(result, options = {})
#         options = defaults.merge(options)
#
#         score = 0.0
#
#         return score unless result
#
#         if person = result.person
#           if person.avatar
#             score += 5
#           end
#
#           if person.twitter.followers
#             score += person.twitter.followers * options.twitter_followers_weight
#           end
#
#           if person.angellist.followers
#             score += person.angellist.followers * options.angellist_followers_weight
#           end
#
#           if person.klout.score
#             score += person.klout.score * options.klout_score_weight
#           end
#         end
#
#         if company = result.company
#           unless company.personal
#             score += options.company_score
#           end
#
#           if company.raised
#             score += company.raised *
#                       options.company_raised_weight
#           end
#
#           if company.employees
#             score += company.employees *
#                       options.company_employees_weight
#           end
#
#           if company.alexa.globalRank
#             score += 1 / (company.alexa.globalRank *
#                       options.company_alexa_rank_weight)
#           end
#
#           if company.google.rank && company.google.rank > 0
#             score += 1 / (company.google.rank *
#                       options.company_google_rank_weight)
#           end
#
#           if company.twitter.followers
#             score += company.twitter.followers *
#                       options.company_twitter_followers_weight
#           end
#         end
#
#         score /= options.total_score
#
#         [score.round(1), 1.0].min
#       end
