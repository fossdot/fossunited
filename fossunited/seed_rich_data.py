"""
Seed rich event data: RSVP forms, volunteer records, CFP + speakers,
sponsors, community partners, and event schedules.
"""
import frappe
from frappe.utils import now_datetime


# ─── Reusable people pools ──────────────────────────────────────────────────

SPEAKERS = [
    {"full_name": "Rushabh Mehta",    "email": "rushabh@erpnext.com",        "designation": "Co-founder & CEO",          "organization": "Frappe Technologies",  "social_link": "https://twitter.com/rushabh_mehta"},
    {"full_name": "Anand Chitipothu", "email": "anand@fossunited.org",        "designation": "Director",                  "organization": "FOSS United",          "social_link": "https://twitter.com/anandology"},
    {"full_name": "Kailash Nadh",     "email": "kailash@zerodha.com",         "designation": "CTO",                       "organization": "Zerodha",              "social_link": "https://twitter.com/knadh"},
    {"full_name": "Praveen Patil",    "email": "praveen@gnowledge.org",        "designation": "Lead Developer",            "organization": "Gnowledge Lab, HBCSE", "social_link": "https://github.com/gnowledge"},
    {"full_name": "Ramaseshan S",     "email": "rams@tamillinux.org",          "designation": "Lead, Tamil Localisation",  "organization": "Tamil FOSS Community", "social_link": "https://twitter.com/tamillinux"},
    {"full_name": "Pirate Praveen",   "email": "praveen@debian.org",           "designation": "Debian Developer",          "organization": "Debian Project",       "social_link": "https://mastodon.social/@piratepraveen"},
    {"full_name": "Subhashish Panigrahi", "email": "subhash@pia.media",       "designation": "Research Director",         "organization": "Access Now India",     "social_link": "https://twitter.com/subhapa"},
    {"full_name": "Vishal Arya",      "email": "vishal@indlinux.org",          "designation": "Community Lead",            "organization": "Indian Linux Users Group", "social_link": "https://twitter.com/vishalarya"},
    {"full_name": "Dhanesh Mane",     "email": "dhanesh@frappe.io",            "designation": "Senior Engineer",           "organization": "Frappe Technologies",  "social_link": "https://github.com/dhanesh"},
    {"full_name": "Lakshmi Narasimhan", "email": "lakshmi@kde.org",           "designation": "KDE Developer",             "organization": "KDE India",            "social_link": "https://twitter.com/lakshmi_kde"},
    {"full_name": "Santhosh Thottingal", "email": "santhosh@wikimedia.org",   "designation": "Senior Software Engineer",  "organization": "Wikimedia Foundation", "social_link": "https://twitter.com/santhoshtr"},
    {"full_name": "Shakthi Kannan",   "email": "shakthi@redhat.com",           "designation": "Software Engineer",         "organization": "Red Hat",              "social_link": "https://twitter.com/shakthimaan"},
    {"full_name": "Arfat Salman",     "email": "arfat@mozilla.com",            "designation": "Developer Advocate",        "organization": "Mozilla",              "social_link": "https://twitter.com/arfatsalman"},
    {"full_name": "Manu Mukerji",     "email": "manu@data.gov.in",             "designation": "Director, Data Policy",     "organization": "Government of India",  "social_link": "https://linkedin.com/in/manumukerji"},
    {"full_name": "Shivam Mathur",    "email": "shivam@php.net",               "designation": "PHP Release Manager",       "organization": "PHP Project",          "social_link": "https://twitter.com/shivam_mathur"},
    {"full_name": "Abhas Abhinav",    "email": "abhas@deeproot.in",            "designation": "Founder",                   "organization": "DeepRoot Linux",       "social_link": "https://twitter.com/abhasabhinav"},
    {"full_name": "Venkatesh Hariharan", "email": "venky@redhat.com",         "designation": "Policy Director",           "organization": "Red Hat India",        "social_link": "https://twitter.com/venkyhariharan"},
    {"full_name": "Manish Sinha",     "email": "manish@gnome.org",             "designation": "GNOME Foundation Member",   "organization": "GNOME Foundation",     "social_link": "https://twitter.com/manishsinha"},
    {"full_name": "Noopur Raval",     "email": "noopur@aiethics.in",           "designation": "AI Ethics Researcher",      "organization": "AI Ethics Lab",        "social_link": "https://twitter.com/noopurraval"},
    {"full_name": "Priyanka Nag",     "email": "priyanka@redhat.com",          "designation": "Open Source Community Mgr", "organization": "Red Hat",              "social_link": "https://twitter.com/priyankanag"},
    {"full_name": "Kushal Das",       "email": "kushal@python.org",            "designation": "CPython Core Developer",    "organization": "Python Software Foundation", "social_link": "https://twitter.com/kushaldas"},
    {"full_name": "Thiyagarajan T",   "email": "thiyagu@tamilwiki.org",        "designation": "Tamil Wikipedia Admin",     "organization": "Tamil Wikipedia",      "social_link": "https://twitter.com/tamilwiki"},
    {"full_name": "Pooja Shah",       "email": "pooja@blender.org",            "designation": "Blender Trainer",           "organization": "Blender India",        "social_link": "https://twitter.com/poojashah_3d"},
    {"full_name": "Roshan Paul",      "email": "roshan@sugarlabs.org",         "designation": "Software Developer",        "organization": "Sugar Labs",           "social_link": "https://github.com/roshanpaul"},
    {"full_name": "Nabarun Pal",      "email": "nabarun@kubernetes.io",        "designation": "Kubernetes Maintainer",     "organization": "Kubernetes Project",   "social_link": "https://twitter.com/palnabarun"},
]

VOLUNTEERS = [
    {"volunteer_name": "Arun Kumar",      "email": "arun.kumar@example.com",    "phone_number": "9876543210", "volunteer_as": "Venue Management",               "bio": "Regular FOSS United volunteer since 2021"},
    {"volunteer_name": "Priya Sharma",    "email": "priya.sharma@example.com",  "phone_number": "9876543211", "volunteer_as": "Marketing",                      "bio": "Design and marketing volunteer"},
    {"volunteer_name": "Rahul Singh",     "email": "rahul.singh@example.com",   "phone_number": "9876543212", "volunteer_as": "Speaker Management",             "bio": "Loves coordinating with speakers"},
    {"volunteer_name": "Sneha Patel",     "email": "sneha.patel@example.com",   "phone_number": "9876543213", "volunteer_as": "Community Outreach",             "bio": "Social media and outreach"},
    {"volunteer_name": "Vikram Reddy",    "email": "vikram.reddy@example.com",  "phone_number": "9876543214", "volunteer_as": "Production and Livestream",      "bio": "AV and livestream volunteer"},
    {"volunteer_name": "Kavya Nair",      "email": "kavya.nair@example.com",    "phone_number": "9876543215", "volunteer_as": "Content",                        "bio": "Content and documentation"},
    {"volunteer_name": "Siddharth Jain",  "email": "siddharth.jain@example.com","phone_number": "9876543216", "volunteer_as": "Travel Desk",                   "bio": "Travel and accommodation coordination"},
    {"volunteer_name": "Deepa Menon",     "email": "deepa.menon@example.com",   "phone_number": "9876543217", "volunteer_as": "Diversity",                      "bio": "Diversity and inclusion lead"},
    {"volunteer_name": "Arjun Iyer",      "email": "arjun.iyer@example.com",    "phone_number": "9876543218", "volunteer_as": "Volunteer Manager",              "bio": "Volunteer coordination and management"},
    {"volunteer_name": "Meera Krishnan",  "email": "meera.krishnan@example.com","phone_number": "9876543219", "volunteer_as": "Design",                        "bio": "UI/UX and visual design"},
    {"volunteer_name": "Rohan Das",       "email": "rohan.das@example.com",     "phone_number": "9876543220", "volunteer_as": "Open Spaces Management",         "bio": "Facilitates open spaces and BoF sessions"},
    {"volunteer_name": "Ananya Ghosh",    "email": "ananya.ghosh@example.com",  "phone_number": "9876543221", "volunteer_as": "Adhoc Jobs Management",          "bio": "Handles on-the-ground logistics"},
    {"volunteer_name": "Tarun Verma",     "email": "tarun.verma@example.com",   "phone_number": "9876543222", "volunteer_as": "Marketing",                      "bio": "Social media and pre-event promotions"},
    {"volunteer_name": "Lakshmi Devi",    "email": "lakshmi.devi@example.com",  "phone_number": "9876543223", "volunteer_as": "Host/Emcees",                    "bio": "Hosts and facilitates sessions"},
    {"volunteer_name": "Karan Mehta",     "email": "karan.mehta@example.com",   "phone_number": "9876543224", "volunteer_as": "Sponsorships",                   "bio": "Sponsor relations and on-site support"},
    {"volunteer_name": "Sunita Rao",      "email": "sunita.rao@example.com",    "phone_number": "9876543225", "volunteer_as": "Video Editing",                  "bio": "Records and edits talk videos"},
    {"volunteer_name": "Manav Shah",      "email": "manav.shah@example.com",    "phone_number": "9876543226", "volunteer_as": "Parallel Sessions Management",   "bio": "Coordinates multi-track events"},
    {"volunteer_name": "Geeta Pillai",    "email": "geeta.pillai@example.com",  "phone_number": "9876543227", "volunteer_as": "Community Outreach",             "bio": "College outreach and student community"},
    {"volunteer_name": "Nitin Kulkarni",  "email": "nitin.kulkarni@example.com","phone_number": "9876543228", "volunteer_as": "Venue Management",              "bio": "Venue setup, signage, and logistics"},
    {"volunteer_name": "Smita Joshi",     "email": "smita.joshi@example.com",   "phone_number": "9876543229", "volunteer_as": "Content",                        "bio": "Documentation and write-ups"},
]

SPONSORS = [
    {"sponsor_name": "Zerodha",        "tier": "Platinum", "link": "https://zerodha.com"},
    {"sponsor_name": "Frappe",         "tier": "Gold",     "link": "https://frappe.io"},
    {"sponsor_name": "Red Hat",        "tier": "Gold",     "link": "https://redhat.com"},
    {"sponsor_name": "Canonical",      "tier": "Silver",   "link": "https://ubuntu.com"},
    {"sponsor_name": "Mozilla",        "tier": "Silver",   "link": "https://mozilla.org"},
    {"sponsor_name": "SFLC.in",        "tier": "Bronze",   "link": "https://sflc.in"},
    {"sponsor_name": "Thoughtworks",   "tier": "Gold",     "link": "https://thoughtworks.com"},
    {"sponsor_name": "GitLab",         "tier": "Silver",   "link": "https://gitlab.com"},
    {"sponsor_name": "DigitalOcean",   "tier": "Bronze",   "link": "https://digitalocean.com"},
    {"sponsor_name": "NIMHANS",        "tier": "Venue Partner", "link": "https://nimhans.ac.in"},
    {"sponsor_name": "IIT Bombay",     "tier": "Venue Partner", "link": "https://iitb.ac.in"},
    {"sponsor_name": "IIIT Hyderabad", "tier": "Venue Partner", "link": "https://iiit.ac.in"},
    {"sponsor_name": "JetBrains",      "tier": "Bronze",   "link": "https://jetbrains.com"},
    {"sponsor_name": "AWS Open Source","tier": "Silver",   "link": "https://aws.amazon.com/opensource"},
    {"sponsor_name": "Linode",         "tier": "Bronze",   "link": "https://linode.com"},
]

COMMUNITY_PARTNERS = [
    {"org_name": "Free Software Movement Karnataka", "link": "https://fsmk.org"},
    {"org_name": "iSPIRT",                           "link": "https://ispirt.in"},
    {"org_name": "Internet Freedom Foundation",      "link": "https://internetfreedom.in"},
    {"org_name": "Python India",                     "link": "https://in.pycon.org"},
    {"org_name": "DGPLUG",                           "link": "https://dgplug.org"},
    {"org_name": "Wikimedia India",                  "link": "https://wikimedia.in"},
    {"org_name": "OpenStreetMap India",              "link": "https://openstreetmap.in"},
    {"org_name": "ILUG-D",                           "link": "https://linux-delhi.org"},
    {"org_name": "BangaloreLUG",                     "link": "https://blug.linux.org.in"},
    {"org_name": "ChennaiPy",                        "link": "https://chennaipy.org"},
    {"org_name": "Hyderabad Python User Group",      "link": "https://hydpug.org"},
    {"org_name": "Pune Linux User Group",            "link": "https://plug.org.in"},
    {"org_name": "KDE India",                        "link": "https://kde.org"},
    {"org_name": "Debian India",                     "link": "https://debian.org.in"},
    {"org_name": "The/Nudge Institute",              "link": "https://thenudge.org"},
]

# ─── Event-specific config ───────────────────────────────────────────────────

# Maps event_permalink → enrichment config
EVENT_ENRICH = {

    # ── Flagship conferences ──────────────────────────────────────────
    "indiafoss-1": {
        "sponsors":   [0,1,2,3,4,5],
        "partners":   [0,1,2,9,13],
        "volunteers": list(range(10)),
        "speakers":   [0,1,2,5,6,7,10,11,13,16,20,21],
        "talks": [
            {"title": "Opening Keynote: The State of FOSS in India",           "type": "Invited Talk", "speakers": [1,2]},
            {"title": "Frappe Framework: Building ERPs with Open Source",       "type": "Talk",         "speakers": [0]},
            {"title": "Digital Public Goods and Open Source",                  "type": "Talk",         "speakers": [13]},
            {"title": "Free Software and Democracy",                           "type": "Talk",         "speakers": [16]},
            {"title": "Localisation at Scale: Indian Languages in FOSS",       "type": "Talk",         "speakers": [10]},
            {"title": "Debian Packaging: Contributing to Universal OS",        "type": "Talk",         "speakers": [5]},
            {"title": "FOSS in Education: Ground Reality",                     "type": "Talk",         "speakers": [3]},
            {"title": "Panel: Sustainability of Open Source Projects",         "type": "Panel Discussion", "speakers": [2,6,15]},
            {"title": "Lightning Talks: Community Projects",                   "type": "Lightning Talk","speakers": [17]},
            {"title": "Closing Note: Future Roadmap for FOSS United",         "type": "Talk",         "speakers": [1]},
        ],
        "rsvp": {"max_rsvp_count": 500, "rsvp_description": "<p>Register to attend India FOSS 1.0 online. You will receive the Jitsi meeting link 24 hours before the event.</p>"},
    },
    "indiafoss-2": {
        "sponsors":   [0,1,2,3,4,5,6,7,9],
        "partners":   [0,1,2,3,4,5,6,7,8,9],
        "volunteers": list(range(15)),
        "speakers":   list(range(20)),
        "talks": [
            {"title": "Opening Keynote: Why India Needs a FOSS Ecosystem",     "type": "Invited Talk", "speakers": [1,2]},
            {"title": "Building on Frappe: Real World Deployments",            "type": "Talk",         "speakers": [0,8]},
            {"title": "GNOME: Past, Present and Future",                       "type": "Talk",         "speakers": [17]},
            {"title": "Internet Freedom and Open Source Law",                  "type": "Talk",         "speakers": [6]},
            {"title": "Python and Open Data in Government",                    "type": "Talk",         "speakers": [13]},
            {"title": "Kubernetes on Bare Metal with Open Source Tools",       "type": "Talk",         "speakers": [24]},
            {"title": "Tamil NLP: Open Source for Indian Languages",           "type": "Talk",         "speakers": [4]},
            {"title": "Sugar Labs: FOSS in Primary Education",                 "type": "Talk",         "speakers": [23]},
            {"title": "Panel: Women in Open Source",                           "type": "Panel Discussion", "speakers": [19,7,21]},
            {"title": "Workshop: First Contribution to Linux Kernel",          "type": "Workshop",     "speakers": [11]},
            {"title": "DeepRoot: 20 Years of Free Software Business in India", "type": "Talk",         "speakers": [15]},
            {"title": "AI and Ethics: An Open Source Perspective",             "type": "Talk",         "speakers": [18]},
            {"title": "Lightning Talks",                                       "type": "Lightning Talk","speakers": [12]},
            {"title": "Closing Keynote: Together We Build",                    "type": "Talk",         "speakers": [2]},
        ],
        "rsvp": {"max_rsvp_count": 1000, "rsvp_description": "<p>Register for India FOSS 2.0. Walk-in entry is also available but registered attendees get priority seating and conference kit.</p>"},
    },
    "indiafoss-3": {
        "sponsors":   [0,1,2,3,4,5,6,7,8,9,12,13,14],
        "partners":   list(range(10)),
        "volunteers": list(range(20)),
        "speakers":   list(range(25)),
        "talks": [
            {"title": "Opening Keynote: FOSS for Bharat",                      "type": "Invited Talk", "speakers": [2,1]},
            {"title": "Zerodha: Building Financial Infrastructure on OSS",     "type": "Talk",         "speakers": [2]},
            {"title": "GNOME 44: What's New and What's Next",                  "type": "Talk",         "speakers": [17]},
            {"title": "PHP 8.3 Release Highlights",                            "type": "Talk",         "speakers": [14]},
            {"title": "Contributing to CPython: A Practical Guide",            "type": "Talk",         "speakers": [20]},
            {"title": "Open Source AI: Responsible Deployment",               "type": "Talk",         "speakers": [18]},
            {"title": "Wikimedia Tech: Scaling Knowledge for All",             "type": "Talk",         "speakers": [10]},
            {"title": "Digital Rights in the Age of AI",                       "type": "Talk",         "speakers": [6,7]},
            {"title": "Panel: FOSS Policy in India — Progress and Gaps",       "type": "Panel Discussion", "speakers": [13,16,6]},
            {"title": "Workshop: Rust Programming for Systems Developers",     "type": "Workshop",     "speakers": [24]},
            {"title": "Workshop: Contributing to Frappe",                      "type": "Workshop",     "speakers": [0,8]},
            {"title": "BoF: FOSS Club Network India",                          "type": "Birds of Feather(BoF)", "speakers": [3]},
            {"title": "Tamil and Indic Language Computing: 2023 Update",       "type": "Talk",         "speakers": [4,21]},
            {"title": "Blender for Open Content Creation",                     "type": "Talk",         "speakers": [22]},
            {"title": "Lightning Talks",                                       "type": "Lightning Talk","speakers": [19]},
            {"title": "Closing Keynote: The Next Chapter",                     "type": "Talk",         "speakers": [1]},
        ],
        "rsvp": {"max_rsvp_count": 1500, "rsvp_description": "<p>Register for India FOSS 3.0. Registered attendees get conference kit, lunch coupons, and priority entry.</p>"},
    },
    "indiafoss-4": {
        "sponsors":   [0,1,2,3,4,5,6,7,8,9,10,12,13,14],
        "partners":   list(range(12)),
        "volunteers": list(range(20)),
        "speakers":   list(range(25)),
        "talks": [
            {"title": "Opening Keynote: Open Source at Scale in India",        "type": "Invited Talk", "speakers": [1,2]},
            {"title": "ERPNext 15: Enterprise Open Source",                    "type": "Talk",         "speakers": [0]},
            {"title": "GNOME 48 Features Overview",                            "type": "Talk",         "speakers": [17]},
            {"title": "Open Source AI Models: State of the Union",             "type": "Talk",         "speakers": [18]},
            {"title": "CPython 3.14: What's Coming",                           "type": "Talk",         "speakers": [20]},
            {"title": "Kubernetes 1.30 and Cloud Native FOSS",                 "type": "Talk",         "speakers": [24]},
            {"title": "Debian 13: Inside the Trixie Release",                  "type": "Talk",         "speakers": [5]},
            {"title": "Digital Public Infrastructure and FOSS",               "type": "Talk",         "speakers": [13]},
            {"title": "Panel: Open Source Policy — India's Opportunity",       "type": "Panel Discussion", "speakers": [13,16,6]},
            {"title": "Workshop: Frappe Framework Deep Dive",                  "type": "Workshop",     "speakers": [0,8]},
            {"title": "Workshop: Open Source Security with eBPF",              "type": "Workshop",     "speakers": [24]},
            {"title": "BoF: FOSS in Education",                                "type": "Birds of Feather(BoF)", "speakers": [3,23]},
            {"title": "BoF: Women in Open Source",                             "type": "Birds of Feather(BoF)", "speakers": [19,22]},
            {"title": "Lightning Talks: Community Projects",                   "type": "Lightning Talk","speakers": [12]},
            {"title": "Closing Keynote",                                       "type": "Talk",         "speakers": [2]},
        ],
        "rsvp": {"max_rsvp_count": 2000, "rsvp_description": "<p>Register for India FOSS 4.0. All registered attendees receive a conference kit and access to the evening community dinner.</p>"},
    },

    # ── FOSS Hack ─────────────────────────────────────────────────────
    "fosshack-1": {
        "sponsors":   [1,4,8],
        "partners":   [0,3,5],
        "volunteers": [0,1,2,4,5],
        "speakers":   [1,2],
        "rsvp": {"max_rsvp_count": 200, "rsvp_description": "<p>Register your team for FOSS Hack 1. Teams of 2–4. All projects must be open-source and submitted to a public repo.</p>"},
    },
    "fosshack-2": {
        "sponsors":   [1,4,7],
        "partners":   [0,3,4],
        "volunteers": [0,1,2,4,5,6],
        "speakers":   [1,2,0],
        "rsvp": {"max_rsvp_count": 300, "rsvp_description": "<p>Register for FOSS Hack 2. Teams of 2–4 members. Theme: Developer tools and productivity.</p>"},
    },
    "fosshack-3": {
        "sponsors":   [0,1,2,4,7,8],
        "partners":   [0,3,4,5],
        "volunteers": list(range(8)),
        "speakers":   [1,2,0,20],
        "rsvp": {"max_rsvp_count": 400, "rsvp_description": "<p>Register for FOSS Hack 3. Hybrid format — choose a localhost venue near you or participate online. Cash prizes for top 3 teams.</p>"},
    },
    "fosshack-4": {
        "sponsors":   [0,1,2,3,4,7,8,12],
        "partners":   [0,3,4,5,6],
        "volunteers": list(range(10)),
        "speakers":   [1,2,0,20,24],
        "rsvp": {"max_rsvp_count": 500, "rsvp_description": "<p>Register for FOSS Hack 4. Teams of 2–4. Six localhost venues across India plus online participation. ₹5L total prize pool.</p>"},
    },

    # ── BangaloreFOSS ─────────────────────────────────────────────────
    "bangalorefoss-2022": {
        "sponsors":   [0,1,2,3,5,9],
        "partners":   [0,2,4,8],
        "volunteers": [0,1,2,3,4,5,6,7,8],
        "speakers":   [0,2,5,7,9,11,15,17,22],
        "talks": [
            {"title": "Opening: Bangalore and FOSS",                           "type": "Invited Talk", "speakers": [2]},
            {"title": "Linux Security: Modern Approaches",                     "type": "Talk",         "speakers": [11]},
            {"title": "Rust: Systems Programming for Everyone",                "type": "Talk",         "speakers": [24]},
            {"title": "KDE Plasma 5: Desktop Freedom",                         "type": "Talk",         "speakers": [9]},
            {"title": "DeepRoot: Running a FOSS Business",                     "type": "Talk",         "speakers": [15]},
            {"title": "Debian Packaging Workshop",                             "type": "Workshop",     "speakers": [5]},
            {"title": "Panel: FOSS Community Governance",                      "type": "Panel Discussion", "speakers": [1,7,17]},
            {"title": "Lightning Talks",                                       "type": "Lightning Talk","speakers": [22]},
        ],
        "rsvp": {"max_rsvp_count": 600, "rsvp_description": "<p>Register for BangaloreFOSS 2022. Free entry with registration.</p>"},
    },
    "bangalorefoss-2023": {
        "sponsors":   [0,1,2,3,4,5,6,9,12],
        "partners":   [0,2,4,8,9,13],
        "volunteers": list(range(12)),
        "speakers":   [0,1,2,5,9,11,14,17,18,20,22,24],
        "talks": [
            {"title": "Opening Keynote",                                       "type": "Invited Talk", "speakers": [2,1]},
            {"title": "AI and Open Source: Complementary or Conflicting?",     "type": "Talk",         "speakers": [18]},
            {"title": "Linux Kernel Security in 2023",                         "type": "Talk",         "speakers": [11]},
            {"title": "PHP 8.3 and Modern PHP Development",                    "type": "Talk",         "speakers": [14]},
            {"title": "Open Source Business Models that Work",                 "type": "Talk",         "speakers": [0]},
            {"title": "Rust in the Linux Kernel",                              "type": "Talk",         "speakers": [24]},
            {"title": "GNOME 45: Redesigned and Refined",                      "type": "Talk",         "speakers": [17]},
            {"title": "Panel: FOSS and Policy in India",                       "type": "Panel Discussion", "speakers": [6,16,13]},
            {"title": "Workshop: Contributing to CPython",                     "type": "Workshop",     "speakers": [20]},
            {"title": "Lightning Talks",                                       "type": "Lightning Talk","speakers": [22]},
        ],
        "rsvp": {"max_rsvp_count": 700, "rsvp_description": "<p>Register for BangaloreFOSS 2023. Conference kit for all registered attendees.</p>"},
    },
    "bangalorefoss-2024": {
        "sponsors":   [0,1,2,3,4,5,6,7,9,12,13],
        "partners":   list(range(10)),
        "volunteers": list(range(15)),
        "speakers":   list(range(20)),
        "talks": [
            {"title": "Opening Keynote: FOSS at the AI Frontier",              "type": "Invited Talk", "speakers": [1,2]},
            {"title": "Open Source LLMs: Where We Stand",                      "type": "Talk",         "speakers": [18]},
            {"title": "Rust in Production: 2024 Update",                       "type": "Talk",         "speakers": [24]},
            {"title": "GNOME 47 and the Wayland Future",                       "type": "Talk",         "speakers": [17]},
            {"title": "Frappe v15: What's New",                                "type": "Talk",         "speakers": [0,8]},
            {"title": "KDE Plasma 6 Deep Dive",                                "type": "Talk",         "speakers": [9]},
            {"title": "Building Privacy-Preserving Apps with FOSS",            "type": "Talk",         "speakers": [19]},
            {"title": "Panel: AI Ethics and Open Source",                      "type": "Panel Discussion", "speakers": [18,16,6]},
            {"title": "Workshop: eBPF for Observability",                      "type": "Workshop",     "speakers": [24]},
            {"title": "Workshop: Contributing to Wikimedia",                   "type": "Workshop",     "speakers": [10]},
            {"title": "BoF: FOSS in Healthcare",                               "type": "Birds of Feather(BoF)", "speakers": [3]},
            {"title": "Lightning Talks",                                       "type": "Lightning Talk","speakers": [12]},
        ],
        "rsvp": {"max_rsvp_count": 800, "rsvp_description": "<p>Register for BangaloreFOSS 2024. Registered attendees get lunch, conference kit, and access to workshops.</p>"},
    },

    # ── PyConf Hyderabad ──────────────────────────────────────────────
    "pyconf-hyderabad-2021": {
        "sponsors":   [1,4,7,8],
        "partners":   [3,5,11],
        "volunteers": [0,1,3,4,5,6],
        "speakers":   [20,2,18,14],
        "talks": [
            {"title": "CPython Internals: Understanding the GIL",              "type": "Talk",         "speakers": [20]},
            {"title": "Data Engineering at Scale with Python",                 "type": "Talk",         "speakers": [2]},
            {"title": "AI Ethics and Python Frameworks",                       "type": "Talk",         "speakers": [18]},
            {"title": "Modern Python Packaging with pip and Poetry",           "type": "Talk",         "speakers": [14]},
            {"title": "Panel: Open Source Python in Indian Startups",         "type": "Panel Discussion", "speakers": [20,2,14]},
        ],
        "rsvp": {"max_rsvp_count": 500, "rsvp_description": "<p>Register for PyConf Hyderabad 2021. Online event — meeting links shared via email.</p>"},
    },
    "pyconf-hyderabad-2022": {
        "sponsors":   [0,1,2,4,7],
        "partners":   [3,4,11,12],
        "volunteers": list(range(8)),
        "speakers":   [20,2,18,14,19],
        "talks": [
            {"title": "Keynote: Python in the Decade of AI",                   "type": "Invited Talk", "speakers": [20]},
            {"title": "Django 4.1: What's New",                                "type": "Talk",         "speakers": [14]},
            {"title": "FastAPI for High-Performance APIs",                     "type": "Talk",         "speakers": [2]},
            {"title": "Responsible AI with Open Source Python",                "type": "Talk",         "speakers": [18]},
            {"title": "Workshop: Data Science with Pandas and Polars",         "type": "Workshop",     "speakers": [19]},
            {"title": "Panel: Python Community in Telangana",                  "type": "Panel Discussion", "speakers": [20,18,2]},
        ],
        "rsvp": {"max_rsvp_count": 500, "rsvp_description": "<p>Register for PyConf Hyderabad 2022. First in-person edition — conference kit included.</p>"},
    },
    "pyconf-hyderabad-2023": {
        "sponsors":   [0,1,2,4,6,7,12],
        "partners":   [3,4,11,12,14],
        "volunteers": list(range(10)),
        "speakers":   [20,2,18,14,19,24],
        "talks": [
            {"title": "Keynote: Python's Role in the Open Source AI Stack",   "type": "Invited Talk", "speakers": [20]},
            {"title": "CPython 3.12 Release Highlights",                       "type": "Talk",         "speakers": [20]},
            {"title": "Building Kubernetes Operators with Python",             "type": "Talk",         "speakers": [24]},
            {"title": "Ethical AI: A Python Developer's Responsibility",       "type": "Talk",         "speakers": [18]},
            {"title": "Django ORM Deep Dive",                                  "type": "Talk",         "speakers": [14]},
            {"title": "Workshop: Building ML Pipelines with FOSS Tools",       "type": "Workshop",     "speakers": [19]},
            {"title": "Panel: Open Source Python in Hyderabad's Tech Scene",  "type": "Panel Discussion", "speakers": [2,18,24]},
        ],
        "rsvp": {"max_rsvp_count": 600, "rsvp_description": "<p>Register for PyConf Hyderabad 2023. Includes lunch and access to all workshops.</p>"},
    },
    "pyconf-hyderabad-2024": {
        "sponsors":   [0,1,2,4,6,7,8,12,13],
        "partners":   [3,4,5,11,12,14],
        "volunteers": list(range(12)),
        "speakers":   [20,2,18,14,19,24,11],
        "talks": [
            {"title": "Keynote: Python in the AI Era",                         "type": "Invited Talk", "speakers": [20]},
            {"title": "CPython 3.13 — No-GIL and Free Threading",              "type": "Talk",         "speakers": [20]},
            {"title": "Building LLM Apps with Open Source Python",             "type": "Talk",         "speakers": [18]},
            {"title": "Security Hardening Django Applications",                "type": "Talk",         "speakers": [11]},
            {"title": "Kubernetes Operators with Python Operator SDK",         "type": "Talk",         "speakers": [24]},
            {"title": "Workshop: Real-world ML with PyTorch + FOSS Data Tools","type": "Workshop",     "speakers": [19]},
            {"title": "Panel: The Next 10 Years of Python in India",           "type": "Panel Discussion", "speakers": [20,2,14]},
        ],
        "rsvp": {"max_rsvp_count": 700, "rsvp_description": "<p>Register for PyConf Hyderabad 2024. Includes conference kit, lunch, and workshop access. First 100 registrations get early bird swag.</p>"},
    },

    # ── PuneFOSS ──────────────────────────────────────────────────────
    "punefoss-2023": {
        "sponsors":   [1,2,4,5,8],
        "partners":   [4,10,11],
        "volunteers": [0,1,4,5,8,9,10],
        "speakers":   [0,3,8,15,23],
        "talks": [
            {"title": "Opening: The Pune FOSS Ecosystem",                      "type": "Invited Talk", "speakers": [8]},
            {"title": "ERPNext for Indian SMEs",                               "type": "Talk",         "speakers": [0]},
            {"title": "Sugar Labs: Open Source in Schools",                    "type": "Talk",         "speakers": [23]},
            {"title": "Open Source in Manufacturing",                          "type": "Talk",         "speakers": [15]},
            {"title": "Panel: Building Sustainable FOSS Communities",         "type": "Panel Discussion", "speakers": [1,3,8]},
        ],
        "rsvp": {"max_rsvp_count": 350, "rsvp_description": "<p>Register for PuneFOSS 2023. Free entry. Students welcome.</p>"},
    },
    "punefoss-2024": {
        "sponsors":   [0,1,2,4,5,8,12],
        "partners":   [4,5,10,11,13],
        "volunteers": list(range(10)),
        "speakers":   [0,3,8,15,18,19,23],
        "talks": [
            {"title": "Opening Keynote: FOSS in Pune Manufacturing 4.0",       "type": "Invited Talk", "speakers": [0]},
            {"title": "ERPNext Case Studies from Pune Industry",               "type": "Talk",         "speakers": [0,8]},
            {"title": "Open Source AI: What Enterprises Should Know",          "type": "Talk",         "speakers": [18]},
            {"title": "Student Project Competition Showcase",                  "type": "Talk",         "speakers": [23]},
            {"title": "Panel: FOSS Funding and Sustainability",                "type": "Panel Discussion", "speakers": [0,15,3]},
            {"title": "Workshop: Getting Started with Frappe",                 "type": "Workshop",     "speakers": [8]},
        ],
        "rsvp": {"max_rsvp_count": 450, "rsvp_description": "<p>Register for PuneFOSS 2024. Includes lunch, workshop access, and conference kit.</p>"},
    },

    # ── City meetups ─────────────────────────────────────────────────
    "blr-meetup-mar-2022": {
        "volunteers": [0,4],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>RSVP for the March 2022 in-person meetup in Bangalore. Limited seats.</p>"},
    },
    "blr-meetup-may-2023": {
        "volunteers": [0,5],
        "rsvp": {"max_rsvp_count": 100, "rsvp_description": "<p>RSVP for the May 2023 Bangalore FOSS meetup.</p>"},
    },
    "blr-meetup-sep-2023": {
        "volunteers": [0,1,5],
        "rsvp": {"max_rsvp_count": 100, "rsvp_description": "<p>RSVP for Bengaluru FOSS Meetup — Hacktoberfest kickoff. Limited seats.</p>"},
    },
    "mumbai-meetup-mar-2023": {
        "volunteers": [0,3],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>RSVP for the Mumbai FOSS meetup — March 2023.</p>"},
    },
    "mumbai-meetup-aug-2023": {
        "volunteers": [0,4],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>RSVP for the Mumbai FOSS meetup — August 2023.</p>"},
    },
    "delhi-meetup-apr-2023": {
        "volunteers": [0,3],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>RSVP for the Delhi FOSS meetup — April 2023.</p>"},
    },
    "delhi-hackathon-2023": {
        "sponsors":   [1,4,8],
        "volunteers": [0,1,2,4,5,6],
        "rsvp": {"max_rsvp_count": 150, "rsvp_description": "<p>Register for the Delhi FOSS Hackathon 2023. Teams of 2–4. 24-hour format.</p>"},
    },
    "chennai-meetup-jun-2023": {
        "volunteers": [0,5],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>RSVP for the Chennai FOSS meetup — June 2023.</p>"},
    },
    "hyd-meetup-may-2023": {
        "volunteers": [0,3],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>RSVP for the Hyderabad FOSS meetup — May 2023.</p>"},
    },
    "kolkata-meetup-may-2023": {
        "volunteers": [0,9],
        "rsvp": {"max_rsvp_count": 60, "rsvp_description": "<p>RSVP for the Kolkata FOSS meetup — May 2023.</p>"},
    },
    "blr-meetup-mar-2024": {
        "volunteers": [0,4,9],
        "rsvp": {"max_rsvp_count": 100, "rsvp_description": "<p>RSVP for the March 2024 Bangalore FOSS meetup.</p>"},
    },
    "blr-meetup-jun-2024": {
        "volunteers": [0,5,9],
        "rsvp": {"max_rsvp_count": 100, "rsvp_description": "<p>RSVP for the June 2024 Bangalore FOSS meetup.</p>"},
    },
    "blr-meetup-oct-2024": {
        "volunteers": [0,1,4],
        "rsvp": {"max_rsvp_count": 120, "rsvp_description": "<p>RSVP for the October 2024 Hacktoberfest meetup in Bangalore.</p>"},
    },
    "mumbai-meetup-may-2024": {
        "volunteers": [0,3],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>RSVP for the Mumbai FOSS meetup — May 2024.</p>"},
    },
    "delhi-meetup-jun-2024": {
        "volunteers": [0,6],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>RSVP for the Delhi FOSS meetup — June 2024.</p>"},
    },
    "iitb-install-fest-2022": {
        "volunteers": [0,1,4,8,9],
        "rsvp": {"max_rsvp_count": 100, "rsvp_description": "<p>Register for the IIT Bombay FOSS Club Install Fest 2022. Bring your laptop with at least 20GB free space.</p>"},
    },
    "iitb-install-fest-2024": {
        "volunteers": [0,1,4,8,9,17],
        "rsvp": {"max_rsvp_count": 120, "rsvp_description": "<p>Register for IITB FOSS Install Fest 2024. Bring a laptop with 20 GB+ free. New this year: 'First PR' track where you make your first open-source contribution.</p>"},
    },
    "nitt-hackathon-2023": {
        "sponsors":   [1,8],
        "volunteers": [0,1,2,4],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>Register for NIT Trichy FOSS Hackathon 2023. Teams of 2–4. 30-hour format.</p>"},
    },
    "nitt-hackathon-2024": {
        "sponsors":   [1,4,8],
        "volunteers": [0,1,2,4,5],
        "rsvp": {"max_rsvp_count": 100, "rsvp_description": "<p>Register for NIT Trichy FOSS Hackathon 2024. 48-hour format. Teams of 2–4.</p>"},
    },
    "bits-sprint-mar-2024": {
        "sponsors":   [1,8],
        "volunteers": [0,1,4],
        "rsvp": {"max_rsvp_count": 50, "rsvp_description": "<p>Register for the BITS Pilani contribution sprint. Weekend format. Bring your laptop and a GitHub account.</p>"},
    },
    "online-meetup-jun-2024": {
        "volunteers": [0,5],
        "rsvp": {"max_rsvp_count": 300, "rsvp_description": "<p>Register for the FOSS United Online Meetup — June 2024. Meeting link will be shared via email.</p>"},
    },
    "online-meetup-nov-2024": {
        "volunteers": [0,5],
        "rsvp": {"max_rsvp_count": 300, "rsvp_description": "<p>Register for the FOSS United Online Meetup — November 2024.</p>"},
    },
    "blr-lip-2023": {
        "volunteers": [0,1,4,8,9,17],
        "rsvp": {"max_rsvp_count": 150, "rsvp_description": "<p>Register for Bengaluru Linux Installation Party 2023. Bring your laptop and a 8 GB USB drive (we will flash it for you).</p>"},
    },
    "delhi-lip-oct-2022": {
        "volunteers": [0,1,4,8],
        "rsvp": {"max_rsvp_count": 80, "rsvp_description": "<p>Register for Delhi Linux Installation Party 2022. Bring your laptop. Minimal Linux knowledge required.</p>"},
    },
    "delhi-linux-workshop-jun-2021": {
        "volunteers": [0,5],
        "rsvp": {"max_rsvp_count": 100, "rsvp_description": "<p>Register for the online Linux workshop. Meeting link will be shared via email 24 hours before the event.</p>"},
    },
    "iitb-oss-workshop-oct-2024": {
        "volunteers": [0,9,17],
        "rsvp": {"max_rsvp_count": 60, "rsvp_description": "<p>Register for the FOSS Club open source workshop series, Session 1 of 3. Beginner-friendly.</p>"},
    },
    "foss-united-launch-2020": {
        "volunteers": [0,1,4,5],
        "rsvp": {"max_rsvp_count": 500, "rsvp_description": "<p>Register for the FOSS United launch online meetup. Meeting link will be shared via email.</p>"},
    },
    "online-meetup-aug-2020": {
        "rsvp": {"max_rsvp_count": 200, "rsvp_description": "<p>Register for the FOSS United national online meetup — August 2020.</p>"},
    },
    "online-meetup-may-2025": {
        "volunteers": [0,5],
        "rsvp": {"max_rsvp_count": 300, "rsvp_description": "<p>Register for the FOSS United Online Meetup — May 2025.</p>"},
    },
}


# ─── Helpers ─────────────────────────────────────────────────────────────────

def get_event(permalink):
    name = frappe.db.get_value("FOSS Chapter Event", {"event_permalink": permalink}, "name")
    if name:
        return frappe.get_doc("FOSS Chapter Event", name)
    return None


def add_sponsors_partners(event, cfg):
    changed = False
    existing_sponsors = {r.sponsor_name for r in event.get("sponsor_list", [])}
    for idx in cfg.get("sponsors", []):
        s = SPONSORS[idx]
        if s["sponsor_name"] not in existing_sponsors:
            event.append("sponsor_list", {
                "sponsor_name": s["sponsor_name"],
                "tier":         s["tier"],
                "link":         s["link"],
                "date_of_confirm": str(event.event_start_date)[:10],
            })
            changed = True

    existing_partners = {r.org_name for r in event.get("community_partners", [])}
    for idx in cfg.get("partners", []):
        p = COMMUNITY_PARTNERS[idx]
        if p["org_name"] not in existing_partners:
            event.append("community_partners", {"org_name": p["org_name"], "link": p["link"]})
            changed = True

    return changed


def add_volunteers(event, cfg):
    event_name_field = event.name
    chapter_field    = event.chapter
    created = 0
    for idx in cfg.get("volunteers", []):
        v = VOLUNTEERS[idx]
        if frappe.db.exists("Event Volunteer", {
            "email": v["email"], "event_linked_field": event_name_field
        }):
            continue
        doc = frappe.get_doc({
            "doctype":            "Event Volunteer",
            "volunteer_name":     v["volunteer_name"],
            "email":              v["email"],
            "phone_number":       v.get("phone_number", ""),
            "bio":                v.get("bio", ""),
            "volunteer_as":       v["volunteer_as"],
            "volunteer_status":   "Accepted",
            "chapter":            chapter_field,
            "event_linked_field": event_name_field,
        })
        doc.insert(ignore_permissions=True)
        created += 1
    return created


def add_cfp_and_submissions(event, cfg):
    """Create a FOSS Event CFP + approved CFP Submissions with speakers."""
    talks = cfg.get("talks")
    if not talks:
        return 0

    # Create CFP form if not exists — must be "Live" for submissions to insert
    cfp_name = frappe.db.get_value("FOSS Event CFP", {"event": event.name}, "name")
    if not cfp_name:
        cfp = frappe.get_doc({
            "doctype":              "FOSS Event CFP",
            "event":                event.name,
            "status":               "Live",
            "cfp_form_description": "<p>Submit a talk, workshop, or panel proposal. All sessions must be relevant to free and open-source software.</p>",
            "deadline":             event.event_start_date,
        })
        cfp.insert(ignore_permissions=True)
        cfp_name = cfp.name
    else:
        # Temporarily mark Live so submissions can be inserted
        frappe.db.set_value("FOSS Event CFP", cfp_name, "status", "Live")

    created = 0
    schedule_rows = []

    for talk in talks:
        title = talk["title"]
        if frappe.db.exists("FOSS Event CFP Submission", {"talk_title": title, "linked_cfp": cfp_name}):
            continue

        # Pick first speaker as primary
        primary_idx = talk["speakers"][0] if talk["speakers"] else 0
        primary_sp  = SPEAKERS[primary_idx % len(SPEAKERS)]

        submission = frappe.get_doc({
            "doctype":     "FOSS Event CFP Submission",
            "linked_cfp":  cfp_name,
            "submitted_by": "Administrator",
            "first_name":  primary_sp["full_name"].split()[0],
            "last_name":   " ".join(primary_sp["full_name"].split()[1:]),
            "full_name":   primary_sp["full_name"],
            "email":       primary_sp["email"],
            "designation": primary_sp["designation"],
            "organization":primary_sp["organization"],
            "bio":         f"{primary_sp['full_name']} is a {primary_sp['designation']} at {primary_sp['organization']}.",
            "talk_title":  title,
            "talk_description": f"<p>{title}. A comprehensive session on open-source technologies and community practices.</p>",
            "session_type":     talk["type"],
            "intended_audience":"Intermediate",
            # Insert as Review Pending (validator requires it), upgrade via db.set_value after
            "status":           "Review Pending",
            "is_published":     1,
            "attendance_confirmed": 1,
            "speakers": [],
        })

        # Add all speakers
        for sp_idx in talk["speakers"]:
            sp = SPEAKERS[sp_idx % len(SPEAKERS)]
            submission.append("speakers", {
                "full_name":    sp["full_name"],
                "email":        sp["email"],
                "designation":  sp["designation"],
                "organization": sp["organization"],
                "bio":          f"{sp['full_name']} is a {sp['designation']} at {sp['organization']}.",
                "social_link":  sp.get("social_link", ""),
            })

        submission.insert(ignore_permissions=True)
        # Bypass status-change validator — mark as Approved directly in DB
        frappe.db.set_value("FOSS Event CFP Submission", submission.name, {
            "status": "Approved",
            "attendance_confirmed": 1,
        })
        created += 1
        schedule_rows.append(submission.name)

    # Set CFP back to Closed now that submissions are in
    frappe.db.set_value("FOSS Event CFP", cfp_name, "status", "Closed")

    # Add event schedule rows
    if schedule_rows and not event.get("event_schedule"):
        event.reload()
        import datetime
        start_date = str(event.event_start_date)[:10]
        base = datetime.datetime(
            int(start_date[:4]), int(start_date[5:7]), int(start_date[8:10]), 9, 0
        )
        for i, sub_name in enumerate(schedule_rows):
            sub = frappe.get_doc("FOSS Event CFP Submission", sub_name)
            s_time = (base + datetime.timedelta(minutes=i*50)).strftime("%H:%M:%S")
            e_time = (base + datetime.timedelta(minutes=i*50+45)).strftime("%H:%M:%S")
            cat_map = {
                "Talk": "Talk", "Workshop": "Workshop",
                "Panel Discussion": "Panel Discussion",
                "Lightning Talk": "Lightning Talk",
                "Invited Talk": "Opening Note",
                "Birds of Feather(BoF)": "Other",
                "Invited Talk": "Talk",
            }
            event.append("event_schedule", {
                "linked_cfp":     sub_name,
                "title":          sub.talk_title,
                "scheduled_date": start_date,
                "start_time":     s_time,
                "end_time":       e_time,
                "category":       cat_map.get(sub.session_type, "Talk"),
                "hall":           "Main Hall" if sub.session_type in ("Opening Note","Talk","Panel Discussion","Lightning Talk") else "Workshop Room",
            })
        event.save(ignore_permissions=True)

    return created


def add_rsvp_form(event, cfg):
    """Create FOSS Event RSVP if not already exists."""
    if not cfg.get("rsvp"):
        return 0
    if frappe.db.exists("FOSS Event RSVP", {"event": event.name}):
        return 0

    rsvp_cfg = cfg["rsvp"]
    rsvp = frappe.get_doc({
        "doctype":           "FOSS Event RSVP",
        "event":             event.name,
        "is_published":      1,
        "max_rsvp_count":    rsvp_cfg.get("max_rsvp_count", 100),
        "rsvp_description":  rsvp_cfg.get("rsvp_description", ""),
        "allow_edit":        1,
        "requires_host_approval": 0,
        "custom_questions": [
            {
                "question":     "How did you hear about this event?",
                "type":         "Select",
                "options":      "Twitter/X\nLinkedIn\nFOSS United website\nWord of mouth\nEmail newsletter\nOther",
                "is_mandatory": 0,
            },
            {
                "question":     "What topics are you most interested in?",
                "type":         "Long Text",
                "is_mandatory": 0,
            },
        ],
    })
    rsvp.insert(ignore_permissions=True)
    return 1


# ─── Main ────────────────────────────────────────────────────────────────────

def run():
    total_vol = total_cfp = total_rsvp = total_events = 0

    for permalink, cfg in EVENT_ENRICH.items():
        event = get_event(permalink)
        if not event:
            print(f"  MISSING event: {permalink}")
            continue

        changed = add_sponsors_partners(event, cfg)
        if changed:
            event.save(ignore_permissions=True)
            event.reload()

        n_vol  = add_volunteers(event, cfg)
        n_cfp  = add_cfp_and_submissions(event, cfg)
        n_rsvp = add_rsvp_form(event, cfg)

        total_vol  += n_vol
        total_cfp  += n_cfp
        total_rsvp += n_rsvp
        total_events += 1

        label = " ".join(filter(None, [
            f"{n_vol}v"  if n_vol  else "",
            f"{n_cfp}t"  if n_cfp  else "",
            f"RSVP"      if n_rsvp else "",
        ]))
        if label:
            print(f"  {event.event_name[:55]:<55}  {label}")

    frappe.db.commit()
    print(f"\nDone — {total_events} events enriched | "
          f"{total_vol} volunteers | {total_cfp} talk submissions | {total_rsvp} RSVP forms")
