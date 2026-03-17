"""
Historical events from 2020 onwards.

Timeline context:
  2020 Jan–Feb  : In-person events
  2020 Mar–Dec  : COVID lockdown → all online
  2021          : Fully online
  2022          : Hybrid — gradually returning to in-person
  2023          : Mostly in-person restored
  2024          : Full in-person
  2025          : Already seeded for recent months; flagship events added here
"""
import frappe


C = {
    "bangalore":  "FOSS United Bangalore-City Community",
    "mumbai":     "FOSS United Mumbai-City Community",
    "delhi":      "FOSS United Delhi-City Community",
    "chennai":    "FOSS United Chennai-City Community",
    "hyderabad":  "FOSS United Hyderabad-City Community",
    "pune":       "FOSS United Pune-City Community",
    "kolkata":    "FOSS United Kolkata-City Community",
    "jaipur":     "FOSS United Jaipur-City Community",
    "iitb":       "FOSS Club IIT Bombay-FOSS Club",
    "bits":       "FOSS Club BITS Pilani-FOSS Club",
    "nitt":       "FOSS Club NIT Trichy-FOSS Club",
    "indiafoss":  "India FOSS-Conference",
    "fosshack":   "FOSS Hack-Conference",
    "pyconf":     "PyConf Hyderabad-Conference",
    "online":     "FOSS United Online-Virtual",
    "diaspora":   "FOSS United Diaspora-Virtual",
}

EVENTS = [

    # ══════════════════════════════════════════════════════════════════════
    # 2020
    # ══════════════════════════════════════════════════════════════════════

    # — Bangalore —
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — January 2020",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-01-25 10:00:00", "event_end_date": "2020-01-25 13:00:00",
        "event_location": "HasGeek House, Domlur, Bangalore",
        "event_bio": "Monthly in-person meetup",
        "event_description": "<p>January 2020 meetup — one of the last in-person gatherings before COVID lockdowns. Talks on Kubernetes and open-source observability.</p>",
        "event_permalink": "blr-meetup-jan-2020", "show_photos": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — February 2020",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-02-22 10:00:00", "event_end_date": "2020-02-22 13:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "February 2020 monthly meetup",
        "event_description": "<p>February meetup featured talks on Rust, open-source fonts, and the state of free software in India.</p>",
        "event_permalink": "blr-meetup-feb-2020", "show_photos": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Online Meetup — May 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-05-30 16:00:00", "event_end_date": "2020-05-30 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "First COVID-era online meetup",
        "event_description": "<p>Our first online meetup post-lockdown. The community quickly adapted, with talks on self-hosting, home-lab setups, and remote collaboration tools.</p>",
        "event_permalink": "blr-online-may-2020",
        "livestream_link": "https://meet.jit.si/fossunited-blr",
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Online Meetup — August 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-08-29 16:00:00", "event_end_date": "2020-08-29 18:00:00",
        "event_location": "Online (BigBlueButton)",
        "event_bio": "Online community meetup — August 2020",
        "event_description": "<p>Talks on open-source alternatives to Zoom, pandemic-era privacy threats, and contributing to Mozilla Firefox.</p>",
        "event_permalink": "blr-online-aug-2020",
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Online Meetup — November 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-11-28 16:00:00", "event_end_date": "2020-11-28 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "November 2020 online meetup",
        "event_description": "<p>Year-end online gathering. Highlights: talks on Matrix, federated social networks, and a retrospective on how the Bangalore FOSS community navigated 2020.</p>",
        "event_permalink": "blr-online-nov-2020",
    },

    # — Mumbai —
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — January 2020",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-01-18 11:00:00", "event_end_date": "2020-01-18 14:00:00",
        "event_location": "VJTI, Matunga, Mumbai",
        "event_bio": "January 2020 — pre-COVID in-person meetup",
        "event_description": "<p>New year kickoff meetup with project showcases, lightning talks, and plans for 2020 events.</p>",
        "event_permalink": "mumbai-meetup-jan-2020", "show_photos": 1,
    },
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Online Meetup — June 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-06-27 16:00:00", "event_end_date": "2020-06-27 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "COVID-era online meetup",
        "event_description": "<p>Talks on decentralised communication, open-source health tools used during the pandemic, and remote pair programming.</p>",
        "event_permalink": "mumbai-online-jun-2020",
    },
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Online Meetup — October 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-10-24 16:00:00", "event_end_date": "2020-10-24 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "October 2020 online meetup",
        "event_description": "<p>Talks on open-source GIS, Linux gaming, and community building in a pandemic.</p>",
        "event_permalink": "mumbai-online-oct-2020",
    },

    # — Delhi —
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Meetup — February 2020",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-02-15 11:00:00", "event_end_date": "2020-02-15 14:00:00",
        "event_location": "IIT Delhi, Hauz Khas",
        "event_bio": "February 2020 in-person meetup",
        "event_description": "<p>Talks on open-source government projects in India, FOSS in education, and a demo of KDE Plasma 5.18.</p>",
        "event_permalink": "delhi-meetup-feb-2020", "show_photos": 1,
    },
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Online Meetup — July 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-07-25 16:00:00", "event_end_date": "2020-07-25 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "July 2020 online meetup",
        "event_description": "<p>Focus on open-source contact tracing apps, digital rights during COVID, and Aarogya Setu's source code release.</p>",
        "event_permalink": "delhi-online-jul-2020",
    },

    # — Chennai —
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Meetup — January 2020",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-01-11 10:00:00", "event_end_date": "2020-01-11 13:00:00",
        "event_location": "Anna University, Guindy, Chennai",
        "event_bio": "January 2020 meetup",
        "event_description": "<p>Topics: Tamil localization of GNOME, open-source in Tamil Nadu government, and a walkthrough of Inkscape 1.0 features.</p>",
        "event_permalink": "chennai-meetup-jan-2020", "show_photos": 1,
    },
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Online Meetup — September 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-09-26 16:00:00", "event_end_date": "2020-09-26 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "Online meetup — September 2020",
        "event_description": "<p>Talks on open-source NLP for Indian languages, LibreOffice contribution guide, and community updates.</p>",
        "event_permalink": "chennai-online-sep-2020",
    },

    # — Hyderabad —
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Meetup — February 2020",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-02-08 11:00:00", "event_end_date": "2020-02-08 14:00:00",
        "event_location": "T-Hub, Raidurgam, Hyderabad",
        "event_bio": "February 2020 meetup",
        "event_description": "<p>Talks on open-source drone software, Python packaging, and FOSS adoption in Hyderabad startups.</p>",
        "event_permalink": "hyd-meetup-feb-2020", "show_photos": 1,
    },
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Online Meetup — October 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-10-17 16:00:00", "event_end_date": "2020-10-17 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "October 2020 online meetup",
        "event_description": "<p>Community check-in, talks on OpenStreetMap, open-source EHR systems, and Hacktoberfest retrospective.</p>",
        "event_permalink": "hyd-online-oct-2020",
    },

    # — FOSS Hack 1 —
    {
        "chapter": C["fosshack"], "event_name": "FOSS Hack 1",
        "event_type": "Hackathon", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-08-01 09:00:00", "event_end_date": "2020-08-02 18:00:00",
        "event_location": "Online",
        "event_bio": "The inaugural FOSS Hack — India's first open-source hackathon by FOSS United",
        "event_description": "<p>FOSS Hack 1 was held fully online during the pandemic. 150+ participants across 40 teams built and improved open-source tools. First edition of what became India's premier FOSS hackathon.</p>",
        "event_permalink": "fosshack-1",
        "show_rsvp": 1, "show_photos": 1, "must_attend": 1,
        "livestream_link": "https://youtube.com/fossunited",
    },

    # — FOSS United Online virtual chapter —
    {
        "chapter": C["online"], "event_name": "FOSS United Launch Online Meetup",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-04-25 16:00:00", "event_end_date": "2020-04-25 18:30:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "Official launch of FOSS United as a national organisation",
        "event_description": "<p>The founding online meetup where FOSS United was formally introduced to the community. City chapters from across India joined to discuss the mission, structure, and roadmap.</p>",
        "event_permalink": "foss-united-launch-2020",
        "livestream_link": "https://youtube.com/fossunited", "show_rsvp": 1, "must_attend": 1,
    },
    {
        "chapter": C["online"], "event_name": "FOSS United Online Meetup — August 2020",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2020-08-29 16:00:00", "event_end_date": "2020-08-29 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "Monthly national online meetup",
        "event_description": "<p>Community-wide online meetup with updates from all city chapters, project showcases, and a talk on FOSS in Indian education.</p>",
        "event_permalink": "online-meetup-aug-2020",
    },

    # ══════════════════════════════════════════════════════════════════════
    # 2021 — all online
    # ══════════════════════════════════════════════════════════════════════

    # — India FOSS 1.0 —
    {
        "chapter": C["indiafoss"], "event_name": "India FOSS 1.0",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-07-24 09:00:00", "event_end_date": "2021-07-25 18:00:00",
        "event_location": "Online",
        "event_bio": "India's first national open-source conference — held online",
        "event_description": "<p>India FOSS 1.0 was the inaugural edition of India's national FOSS conference, held fully online due to COVID-19. 1200+ attendees, 35 talks across 3 tracks, and community meetups in 8 cities.</p>",
        "event_permalink": "indiafoss-1",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
        "livestream_link": "https://youtube.com/fossunited",
    },

    # — FOSS Hack 2 —
    {
        "chapter": C["fosshack"], "event_name": "FOSS Hack 2",
        "event_type": "Hackathon", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-03-20 09:00:00", "event_end_date": "2021-03-21 18:00:00",
        "event_location": "Online",
        "event_bio": "Second edition — fully online",
        "event_description": "<p>FOSS Hack 2 saw 250+ participants across 65 teams. Fully online format. Projects ranged from developer tooling to educational software. Winner: a Frappe-based FOSS project management tool.</p>",
        "event_permalink": "fosshack-2",
        "show_rsvp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Bangalore —
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Online Meetup — March 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-03-27 16:00:00", "event_end_date": "2021-03-27 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "March 2021 online meetup",
        "event_description": "<p>Talks on Blender 2.93, open-source vaccine management systems, and digital divide in India.</p>",
        "event_permalink": "blr-online-mar-2021",
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Online Meetup — July 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-07-31 16:00:00", "event_end_date": "2021-07-31 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "July 2021 online meetup",
        "event_description": "<p>Topics: GNOME 40 release, self-hosted cloud alternatives, and how to contribute to Linux kernel.</p>",
        "event_permalink": "blr-online-jul-2021",
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Online Meetup — November 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-11-27 16:00:00", "event_end_date": "2021-11-27 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "November 2021 online meetup",
        "event_description": "<p>Talks on Nextcloud, ActivityPub and the fediverse, and a Q&A with India FOSS 1.0 organizers.</p>",
        "event_permalink": "blr-online-nov-2021",
    },

    # — Mumbai —
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Online Meetup — April 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-04-24 16:00:00", "event_end_date": "2021-04-24 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "April 2021 online meetup",
        "event_description": "<p>Topics: Signal vs Telegram, open-source mapping with OSM, and FOSS United's first anniversary retrospective.</p>",
        "event_permalink": "mumbai-online-apr-2021",
    },
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Online Meetup — September 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-09-25 16:00:00", "event_end_date": "2021-09-25 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "September 2021 online meetup",
        "event_description": "<p>Talks on open-source robotics, Hacktoberfest planning, and contributor spotlights.</p>",
        "event_permalink": "mumbai-online-sep-2021",
    },

    # — Delhi —
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Online Workshop: Intro to Linux",
        "event_type": "Workshop", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-06-19 10:00:00", "event_end_date": "2021-06-19 14:00:00",
        "event_location": "Online (Zoom)",
        "event_bio": "Beginner Linux workshop held online",
        "event_description": "<p>A 4-hour hands-on online workshop covering Linux basics, the terminal, package management, and customizing a desktop environment. 80 participants attended live.</p>",
        "event_permalink": "delhi-linux-workshop-jun-2021",
        "show_rsvp": 1,
    },
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Online Meetup — October 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-10-30 16:00:00", "event_end_date": "2021-10-30 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "October 2021 online meetup",
        "event_description": "<p>Talks on open-source cybersecurity tools, Hacktoberfest contributions, and a panel on women in FOSS.</p>",
        "event_permalink": "delhi-online-oct-2021",
    },

    # — Chennai —
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Online Meetup — May 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-05-29 16:00:00", "event_end_date": "2021-05-29 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "May 2021 online meetup",
        "event_description": "<p>Talks on open-source Dravidian language computing, LibreOffice Writer tips, and FOSS tools for educators.</p>",
        "event_permalink": "chennai-online-may-2021",
    },
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Online Meetup — October 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-10-23 16:00:00", "event_end_date": "2021-10-23 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "October 2021 online meetup",
        "event_description": "<p>Topics: Tamil Wikipedia contributions, open data in Tamil Nadu, and an intro to Fedora Project.</p>",
        "event_permalink": "chennai-online-oct-2021",
    },

    # — Hyderabad —
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Online Meetup — June 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-06-26 16:00:00", "event_end_date": "2021-06-26 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "June 2021 online meetup",
        "event_description": "<p>Talks on open-source COVID data dashboards, Zulip open-source contributions, and Python 3.10 new features.</p>",
        "event_permalink": "hyd-online-jun-2021",
    },
    {
        "chapter": C["hyderabad"], "event_name": "PyConf Hyderabad 2021 (Online)",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-11-20 09:00:00", "event_end_date": "2021-11-21 18:00:00",
        "event_location": "Online",
        "event_bio": "PyConf Hyderabad 2021 — first edition, held online",
        "event_description": "<p>The inaugural PyConf Hyderabad brought together 400+ Python enthusiasts online for two days of talks on web development, data science, and open-source Python tools.</p>",
        "event_permalink": "pyconf-hyderabad-2021",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "must_attend": 1,
        "livestream_link": "https://youtube.com/pyconfhyd",
    },

    # — Pune —
    {
        "chapter": C["pune"], "event_name": "Pune FOSS Online Meetup — August 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-08-28 16:00:00", "event_end_date": "2021-08-28 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "August 2021 online meetup",
        "event_description": "<p>Talks on ERPNext, open-source supply chain tools, and a student contributor spotlight.</p>",
        "event_permalink": "pune-online-aug-2021",
    },

    # — FOSS Clubs 2021 —
    {
        "chapter": C["iitb"], "event_name": "IIT Bombay FOSS Club — Online Orientation 2021",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2021-08-14 15:00:00", "event_end_date": "2021-08-14 17:00:00",
        "event_location": "Online (MS Teams)",
        "event_bio": "Online orientation for new FOSS Club members",
        "event_description": "<p>Annual orientation for incoming IIT Bombay students introducing them to free software, the club's activities, and open-source contribution pathways.</p>",
        "event_permalink": "iitb-orientation-2021",
        "show_rsvp": 1,
    },

    # ══════════════════════════════════════════════════════════════════════
    # 2022 — hybrid return to in-person
    # ══════════════════════════════════════════════════════════════════════

    # — India FOSS 2.0 —
    {
        "chapter": C["indiafoss"], "event_name": "India FOSS 2.0",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-07-23 09:00:00", "event_end_date": "2022-07-24 18:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "India FOSS 2.0 — first in-person edition",
        "event_description": "<p>India FOSS 2.0 was the first in-person edition, drawing 1000+ attendees after two online years. 50 talks, 25 exhibitors, and 4 tracks. Theme: FOSS in India — past, present, future.</p>",
        "event_permalink": "indiafoss-2",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — FOSS Hack 3 —
    {
        "chapter": C["fosshack"], "event_name": "FOSS Hack 3",
        "event_type": "Hackathon", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-09-24 09:00:00", "event_end_date": "2022-09-25 18:00:00",
        "event_location": "Online + Localhost venues in 6 cities",
        "event_bio": "FOSS Hack 3 — hybrid format with localhost venues",
        "event_description": "<p>FOSS Hack 3 introduced localhost venues — physical hubs across 6 Indian cities — alongside online participation. 320 participants, 80 teams. First edition with cash prizes.</p>",
        "event_permalink": "fosshack-3",
        "show_rsvp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Bangalore —
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — March 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-03-26 10:00:00", "event_end_date": "2022-03-26 13:00:00",
        "event_location": "HasGeek House, Domlur, Bangalore",
        "event_bio": "First in-person meetup after COVID restrictions lifted",
        "event_description": "<p>Our first in-person meetup since February 2020! Great energy and enthusiasm from the community. Talks on GNOME 42, NixOS, and a panel on 2 years of online FOSS community building.</p>",
        "event_permalink": "blr-meetup-mar-2022", "show_photos": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — June 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-06-25 10:00:00", "event_end_date": "2022-06-25 13:00:00",
        "event_location": "91springboard, Koramangala, Bangalore",
        "event_bio": "June 2022 in-person meetup",
        "event_description": "<p>Talks on Wayland adoption, open-source AI tools, and a hands-on intro to contributing to GNOME.</p>",
        "event_permalink": "blr-meetup-jun-2022", "show_photos": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — October 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-10-29 10:00:00", "event_end_date": "2022-10-29 13:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "October 2022 meetup with Hacktoberfest theme",
        "event_description": "<p>Hacktoberfest-themed meetup with contributor walkthroughs, live PRs, and talk on first-time contributions to FOSS projects.</p>",
        "event_permalink": "blr-meetup-oct-2022", "show_photos": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "BangaloreFOSS 2022",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-12-10 09:00:00", "event_end_date": "2022-12-11 18:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "Annual Bangalore city FOSS conference",
        "event_description": "<p>BangaloreFOSS 2022 brought together 500+ attendees for 2 days of talks, workshops, and project demos. Tracks: systems, web, communities, and FOSS policy.</p>",
        "event_permalink": "bangalorefoss-2022",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Mumbai —
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — April 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-04-23 11:00:00", "event_end_date": "2022-04-23 14:00:00",
        "event_location": "IIT Bombay, Powai, Mumbai",
        "event_bio": "First post-COVID in-person meetup in Mumbai",
        "event_description": "<p>Mumbai's long-awaited return to in-person meetups. Talks on LibreOffice, Firefox container tabs, and the future of open-source in Indian fintech.</p>",
        "event_permalink": "mumbai-meetup-apr-2022", "show_photos": 1,
    },
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — September 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-09-24 11:00:00", "event_end_date": "2022-09-24 14:00:00",
        "event_location": "Bombay Connect, Andheri East, Mumbai",
        "event_bio": "September 2022 meetup",
        "event_description": "<p>Talks on self-hosted services, open-source Kubernetes operators, and a lightning talk session from community members.</p>",
        "event_permalink": "mumbai-meetup-sep-2022", "show_photos": 1,
    },

    # — Delhi —
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Meetup — May 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-05-28 11:00:00", "event_end_date": "2022-05-28 14:00:00",
        "event_location": "Delhivery HQ, Gurugram",
        "event_bio": "First in-person Delhi FOSS meetup since 2020",
        "event_description": "<p>Back in person! Talks on FOSS adoption in Indian government, OpenStreetMap, and a community discussion on the Delhi chapter's plans for 2022–23.</p>",
        "event_permalink": "delhi-meetup-may-2022", "show_photos": 1,
    },
    {
        "chapter": C["delhi"], "event_name": "Delhi Linux Installation Party 2022",
        "event_type": "Linux Installation Party", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-10-15 10:00:00", "event_end_date": "2022-10-15 16:00:00",
        "event_location": "Delhi Technological University",
        "event_bio": "Help students switch to Linux",
        "event_description": "<p>50 students came with Windows laptops and left with Linux. Distros installed: Ubuntu (30), Fedora (12), Debian (8). Free stickers and community lunch.</p>",
        "event_permalink": "delhi-lip-oct-2022", "show_photos": 1, "show_rsvp": 1,
    },

    # — Chennai —
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Meetup — April 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-04-30 10:00:00", "event_end_date": "2022-04-30 13:00:00",
        "event_location": "IIT Madras Research Park, Chennai",
        "event_bio": "First in-person Chennai FOSS meetup post COVID",
        "event_description": "<p>Homecoming meetup for the Chennai FOSS community. Talks on FOSS in Tamil education, open street maps for Chennai, and upcoming plans for 2022.</p>",
        "event_permalink": "chennai-meetup-apr-2022", "show_photos": 1,
    },
    {
        "chapter": C["chennai"], "event_name": "ChennaiPy + FOSS United: PyCon Satellite",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-09-17 09:00:00", "event_end_date": "2022-09-17 18:00:00",
        "event_location": "SSN College of Engineering, Chennai",
        "event_bio": "PyCon India 2022 satellite event in Chennai",
        "event_description": "<p>A satellite event co-organised with ChennaiPy for the Python community in Tamil Nadu, featuring local Python speakers and lightning talks.</p>",
        "event_permalink": "chennai-pycon-satellite-2022", "show_speakers": 1, "show_photos": 1,
    },

    # — Hyderabad —
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Meetup — April 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-04-30 11:00:00", "event_end_date": "2022-04-30 14:00:00",
        "event_location": "IIIT Hyderabad, Gachibowli",
        "event_bio": "First in-person Hyderabad meetup post COVID",
        "event_description": "<p>Welcome back! 70 attendees for Hyderabad's first in-person FOSS meetup since early 2020. Talks on Zulip, open-source in Indian startups.</p>",
        "event_permalink": "hyd-meetup-apr-2022", "show_photos": 1,
    },
    {
        "chapter": C["hyderabad"], "event_name": "PyConf Hyderabad 2022",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-12-03 09:00:00", "event_end_date": "2022-12-04 18:00:00",
        "event_location": "HICC, Novotel, Hyderabad",
        "event_bio": "PyConf Hyderabad 2022 — first in-person edition",
        "event_description": "<p>PyConf Hyderabad 2022 marked the first in-person Python conference in Hyderabad. 450+ attendees, 30 talks, workshops on data science, web, and DevOps.</p>",
        "event_permalink": "pyconf-hyderabad-2022",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Pune —
    {
        "chapter": C["pune"], "event_name": "Pune FOSS Meetup — June 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-06-25 11:00:00", "event_end_date": "2022-06-25 14:00:00",
        "event_location": "Persistent Systems, Pune",
        "event_bio": "First in-person Pune FOSS meetup since 2020",
        "event_description": "<p>Welcome back to in-person events in Pune. Talks on ERPNext, Frappe internals, and a community discussion on the Pune open-source ecosystem.</p>",
        "event_permalink": "pune-meetup-jun-2022", "show_photos": 1,
    },

    # — Kolkata —
    {
        "chapter": C["kolkata"], "event_name": "Kolkata FOSS Meetup — July 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-07-30 11:00:00", "event_end_date": "2022-07-30 14:00:00",
        "event_location": "IEM Campus, EM Bypass, Kolkata",
        "event_bio": "First in-person Kolkata FOSS meetup post COVID",
        "event_description": "<p>Kolkata's FOSS community reconnected in person with talks on Bengali Wikipedia, GNOME localisation, and FOSS tools for journalists.</p>",
        "event_permalink": "kolkata-meetup-jul-2022", "show_photos": 1,
    },

    # — FOSS Club events 2022 —
    {
        "chapter": C["iitb"], "event_name": "IIT Bombay FOSS Club — Install Fest 2022",
        "event_type": "Linux Installation Party", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-08-13 10:00:00", "event_end_date": "2022-08-13 16:00:00",
        "event_location": "Student Activity Centre, IIT Bombay",
        "event_bio": "Annual Linux install fest at IITB",
        "event_description": "<p>60+ students got Linux installed on their machines. Most popular distro: Ubuntu. Also covered: dual boot setup, partitioning, and basic terminal usage.</p>",
        "event_permalink": "iitb-install-fest-2022", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["nitt"], "event_name": "NIT Trichy FOSS Club — Orientation 2022",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2022-08-20 15:00:00", "event_end_date": "2022-08-20 17:00:00",
        "event_location": "Central Lecture Theatre, NIT Trichy",
        "event_bio": "Orientation for new FOSS Club members",
        "event_description": "<p>Introduction to free software, the club's activities, GSoC guidance, and a live demo of Linux installation for new students.</p>",
        "event_permalink": "nitt-orientation-2022", "show_rsvp": 1,
    },

    # ══════════════════════════════════════════════════════════════════════
    # 2023 — full in-person restored
    # ══════════════════════════════════════════════════════════════════════

    # — India FOSS 3.0 —
    {
        "chapter": C["indiafoss"], "event_name": "India FOSS 3.0",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-07-29 09:00:00", "event_end_date": "2023-07-30 18:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "India FOSS 3.0 — biggest edition yet at the time",
        "event_description": "<p>India FOSS 3.0 set a new record with 1500+ attendees, 65 talks across 4 tracks, 35 exhibitors, and 200+ volunteers. First edition with a dedicated policy and legal track.</p>",
        "event_permalink": "indiafoss-3",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Bangalore —
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — February 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-02-25 10:00:00", "event_end_date": "2023-02-25 13:00:00",
        "event_location": "HasGeek House, Domlur, Bangalore",
        "event_bio": "February 2023 monthly meetup",
        "event_description": "<p>Talks on GNOME 44, systemd containers, and a deep-dive into Mozilla's open-source strategy.</p>",
        "event_permalink": "blr-meetup-feb-2023", "show_photos": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — May 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-05-27 10:00:00", "event_end_date": "2023-05-27 13:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "May 2023 monthly meetup",
        "event_description": "<p>Talks on contributing to GCC, open-source ML frameworks, and a community project showcase.</p>",
        "event_permalink": "blr-meetup-may-2023", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — September 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-09-30 10:00:00", "event_end_date": "2023-09-30 13:00:00",
        "event_location": "HasGeek House, Bangalore",
        "event_bio": "September 2023 — Hacktoberfest kickoff",
        "event_description": "<p>Hacktoberfest kickoff meetup. Find a project, get guidance from experienced contributors, and make your first PR. Beginner-friendly.</p>",
        "event_permalink": "blr-meetup-sep-2023", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "BangaloreFOSS 2023",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-11-11 09:00:00", "event_end_date": "2023-11-12 18:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "BangaloreFOSS 2023 — annual city conference",
        "event_description": "<p>BangaloreFOSS 2023 hosted 650+ attendees across 2 days with talks on AI/open-source, Linux security, Rust systems programming, and community governance.</p>",
        "event_permalink": "bangalorefoss-2023",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru Linux Installation Party 2023",
        "event_type": "Linux Installation Party", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-04-15 10:00:00", "event_end_date": "2023-04-15 16:00:00",
        "event_location": "Christ University, Hosur Road, Bangalore",
        "event_bio": "Annual Linux install fest in Bangalore",
        "event_description": "<p>100+ students and professionals got help installing Linux. Longest session went to a tricky dual-boot with BitLocker — solved in 45 minutes!</p>",
        "event_permalink": "blr-lip-2023", "show_rsvp": 1, "show_photos": 1,
    },

    # — Mumbai —
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — March 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-03-25 11:00:00", "event_end_date": "2023-03-25 14:00:00",
        "event_location": "Bombay Connect, Andheri East, Mumbai",
        "event_bio": "March 2023 monthly meetup",
        "event_description": "<p>Talks on open-source fintech in India, contributing to KDE Plasma, and a community project showcase.</p>",
        "event_permalink": "mumbai-meetup-mar-2023", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — August 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-08-26 11:00:00", "event_end_date": "2023-08-26 14:00:00",
        "event_location": "IIT Bombay, Powai, Mumbai",
        "event_bio": "August 2023 monthly meetup",
        "event_description": "<p>Talks on open-source LLMs, Podman vs Docker, and a walkthrough of contributing to the Servo browser engine.</p>",
        "event_permalink": "mumbai-meetup-aug-2023", "show_photos": 1, "show_rsvp": 1,
    },

    # — Delhi —
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Meetup — April 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-04-22 11:00:00", "event_end_date": "2023-04-22 14:00:00",
        "event_location": "IIT Delhi, Hauz Khas",
        "event_bio": "April 2023 monthly meetup",
        "event_description": "<p>Talks on digital public infrastructure (DPI) in India, open-source mapping, and a panel on FOSS in Indian government systems.</p>",
        "event_permalink": "delhi-meetup-apr-2023", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Hackathon 2023",
        "event_type": "Hackathon", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-10-21 09:00:00", "event_end_date": "2023-10-22 18:00:00",
        "event_location": "DTU, Rohini, New Delhi",
        "event_bio": "24-hour open-source hackathon in Delhi",
        "event_description": "<p>Delhi's first dedicated open-source hackathon. 120 participants, 28 teams, with projects across government transparency, accessibility tools, and education software.</p>",
        "event_permalink": "delhi-hackathon-2023", "show_rsvp": 1, "show_photos": 1,
    },

    # — Chennai —
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Meetup — June 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-06-24 10:00:00", "event_end_date": "2023-06-24 13:00:00",
        "event_location": "IIT Madras Research Park, Chennai",
        "event_bio": "June 2023 monthly meetup",
        "event_description": "<p>Talks on Tamil language support in open-source tools, Linux gaming on ARM, and contributing to Fedora Project India.</p>",
        "event_permalink": "chennai-meetup-jun-2023", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Meetup — November 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-11-25 10:00:00", "event_end_date": "2023-11-25 13:00:00",
        "event_location": "SSN College of Engineering, Chennai",
        "event_bio": "November 2023 monthly meetup",
        "event_description": "<p>Talks on open-source AI in Tamil NLP, LibreOffice Calc automation, and a retrospective on India FOSS 3.0 participation.</p>",
        "event_permalink": "chennai-meetup-nov-2023", "show_photos": 1, "show_rsvp": 1,
    },

    # — Hyderabad —
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Meetup — May 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-05-27 11:00:00", "event_end_date": "2023-05-27 14:00:00",
        "event_location": "T-Hub, Raidurgam, Hyderabad",
        "event_bio": "May 2023 monthly meetup",
        "event_description": "<p>Talks on open-source ERP for SMEs, Matrix chat protocol, and a community showcase of ongoing FOSS projects.</p>",
        "event_permalink": "hyd-meetup-may-2023", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["hyderabad"], "event_name": "PyConf Hyderabad 2023",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-12-02 09:00:00", "event_end_date": "2023-12-03 18:00:00",
        "event_location": "IIIT Hyderabad, Gachibowli",
        "event_bio": "PyConf Hyderabad 2023 — record attendance",
        "event_description": "<p>PyConf Hyderabad 2023 saw record attendance of 550+. Tracks: web, data science, AI/ML, and open-source contribution. Keynote by a CPython core developer.</p>",
        "event_permalink": "pyconf-hyderabad-2023",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Pune —
    {
        "chapter": C["pune"], "event_name": "Pune FOSS Meetup — April 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-04-29 11:00:00", "event_end_date": "2023-04-29 14:00:00",
        "event_location": "CoWork Cafe, Kothrud, Pune",
        "event_bio": "April 2023 monthly meetup",
        "event_description": "<p>Talks on Frappe framework internals, open-source contribution to ERPNext, and a community showcase.</p>",
        "event_permalink": "pune-meetup-apr-2023", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["pune"], "event_name": "PuneFOSS 2023",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-09-16 09:00:00", "event_end_date": "2023-09-16 18:00:00",
        "event_location": "Symbiosis International University, Pune",
        "event_bio": "Pune's first city FOSS conference",
        "event_description": "<p>PuneFOSS 2023 was Pune's inaugural city-level open-source conference. 300 attendees, 18 talks, and a project showcase featuring local open-source companies.</p>",
        "event_permalink": "punefoss-2023",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Kolkata —
    {
        "chapter": C["kolkata"], "event_name": "Kolkata FOSS Meetup — May 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-05-27 11:00:00", "event_end_date": "2023-05-27 14:00:00",
        "event_location": "Webel Bhavan, Salt Lake, Kolkata",
        "event_bio": "May 2023 monthly meetup",
        "event_description": "<p>Talks on contributing to Bengali Wikipedia, open-source tools in West Bengal government, and an intro to Inkscape for designers.</p>",
        "event_permalink": "kolkata-meetup-may-2023", "show_photos": 1, "show_rsvp": 1,
    },

    # — FOSS Clubs 2023 —
    {
        "chapter": C["iitb"], "event_name": "IIT Bombay FOSS Club — GSoC Result Celebration 2023",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-09-02 16:00:00", "event_end_date": "2023-09-02 18:00:00",
        "event_location": "OAT, IIT Bombay",
        "event_bio": "Celebrating IITB students selected for GSoC 2023",
        "event_description": "<p>12 IIT Bombay students were selected for GSoC 2023. We celebrated their achievement and had them share their project experiences with the club.</p>",
        "event_permalink": "iitb-gsoc-celebrate-2023", "show_photos": 1,
    },
    {
        "chapter": C["nitt"], "event_name": "NIT Trichy FOSS Hackathon 2023",
        "event_type": "Hackathon", "status": "Concluded", "is_published": 1,
        "event_start_date": "2023-03-11 09:00:00", "event_end_date": "2023-03-12 18:00:00",
        "event_location": "CS Department, NIT Trichy",
        "event_bio": "Annual open-source hackathon at NIT Trichy",
        "event_description": "<p>30-hour hackathon with 60 participants across 15 teams. Winning project: an open-source attendance management system for colleges.</p>",
        "event_permalink": "nitt-hackathon-2023", "show_rsvp": 1, "show_photos": 1,
    },

    # ══════════════════════════════════════════════════════════════════════
    # 2024
    # ══════════════════════════════════════════════════════════════════════

    # — Bangalore —
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — March 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-03-30 10:00:00", "event_end_date": "2024-03-30 13:00:00",
        "event_location": "HasGeek House, Domlur, Bangalore",
        "event_bio": "March 2024 monthly meetup",
        "event_description": "<p>Talks on GNOME 46, open-source AI governance, and a demo of the KDE End of 10 campaign to migrate Windows 10 users to Linux.</p>",
        "event_permalink": "blr-meetup-mar-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — June 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-06-29 10:00:00", "event_end_date": "2024-06-29 13:00:00",
        "event_location": "91springboard, Koramangala, Bangalore",
        "event_bio": "June 2024 monthly meetup",
        "event_description": "<p>Talks on Rust in the Linux kernel, open-source observability stack, and a community discussion on GSoC/Outreachy mentoring.</p>",
        "event_permalink": "blr-meetup-jun-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — October 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-10-26 10:00:00", "event_end_date": "2024-10-26 13:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "October 2024 meetup — Hacktoberfest theme",
        "event_description": "<p>Hacktoberfest 2024 edition. Live contribution sessions, PR reviews, and talks on beginner-friendly FOSS projects to contribute to.</p>",
        "event_permalink": "blr-meetup-oct-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "BangaloreFOSS 2024",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-11-09 09:00:00", "event_end_date": "2024-11-10 18:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "BangaloreFOSS 2024 — annual city conference",
        "event_description": "<p>BangaloreFOSS 2024 hosted 750+ attendees with 5 tracks covering AI and open source, Linux ecosystem, web tooling, communities, and policy. Featured 45 speakers and 30 exhibitors.</p>",
        "event_permalink": "bangalorefoss-2024",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Mumbai —
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — May 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-05-25 11:00:00", "event_end_date": "2024-05-25 14:00:00",
        "event_location": "Bombay Connect, Andheri East, Mumbai",
        "event_bio": "May 2024 monthly meetup",
        "event_description": "<p>Talks on Nix and NixOS, open-source LLM inference, and community spotlight on Mumbai FOSS contributors.</p>",
        "event_permalink": "mumbai-meetup-may-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — November 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-11-23 11:00:00", "event_end_date": "2024-11-23 14:00:00",
        "event_location": "IIT Bombay, Powai, Mumbai",
        "event_bio": "November 2024 monthly meetup",
        "event_description": "<p>Talks on open-source AI models, privacy-preserving technologies, and a live demo of self-hosted productivity tools.</p>",
        "event_permalink": "mumbai-meetup-nov-2024", "show_photos": 1, "show_rsvp": 1,
    },

    # — Delhi —
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Meetup — June 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-06-22 11:00:00", "event_end_date": "2024-06-22 14:00:00",
        "event_location": "Delhivery HQ, Gurugram",
        "event_bio": "June 2024 monthly meetup",
        "event_description": "<p>Talks on FOSS in Indian elections (EVM alternatives discussion), open-source alternatives for government software, and digital public goods.</p>",
        "event_permalink": "delhi-meetup-jun-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Birds of a Feather: AI & FOSS",
        "event_type": "Birds Of Feathers", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-09-21 15:00:00", "event_end_date": "2024-09-21 18:00:00",
        "event_location": "IIT Delhi, Hauz Khas",
        "event_bio": "BoF on open-source AI and its intersection with FOSS values",
        "event_description": "<p>Informal discussion on open-weight vs truly open AI models, the future of FOSS in an AI-driven world, and India's role in open-source AI development.</p>",
        "event_permalink": "delhi-bof-ai-sep-2024",
    },

    # — Chennai —
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Meetup — April 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-04-27 10:00:00", "event_end_date": "2024-04-27 13:00:00",
        "event_location": "IIT Madras Research Park, Chennai",
        "event_bio": "April 2024 monthly meetup",
        "event_description": "<p>Talks on Tamil Wikipedia milestones, open-source in Chennai startups, and a demo of Blender for 3D content creators.</p>",
        "event_permalink": "chennai-meetup-apr-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Meetup — September 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-09-28 10:00:00", "event_end_date": "2024-09-28 13:00:00",
        "event_location": "SSN College of Engineering, Chennai",
        "event_bio": "September 2024 monthly meetup",
        "event_description": "<p>Talks on open-source Tamil OCR, Fedora 40 features, and a walkthrough of the Outreachy application process.</p>",
        "event_permalink": "chennai-meetup-sep-2024", "show_photos": 1, "show_rsvp": 1,
    },

    # — Hyderabad —
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Meetup — April 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-04-27 11:00:00", "event_end_date": "2024-04-27 14:00:00",
        "event_location": "IIIT Hyderabad, Gachibowli",
        "event_bio": "April 2024 monthly meetup",
        "event_description": "<p>Talks on Zulip 8.0 release, open-source data engineering tools, and FOSS project sustainability models.</p>",
        "event_permalink": "hyd-meetup-apr-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Meetup — September 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-09-28 11:00:00", "event_end_date": "2024-09-28 14:00:00",
        "event_location": "T-Hub, Raidurgam, Hyderabad",
        "event_bio": "September 2024 monthly meetup",
        "event_description": "<p>Topics: KDE Plasma 6, open-source for Telugu language, and a live coding session on contributing to open-source Python libraries.</p>",
        "event_permalink": "hyd-meetup-sep-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["hyderabad"], "event_name": "PyConf Hyderabad 2024",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-12-07 09:00:00", "event_end_date": "2024-12-08 18:00:00",
        "event_location": "IIIT Hyderabad, Gachibowli",
        "event_bio": "PyConf Hyderabad 2024 — biggest Python conference in Hyderabad",
        "event_description": "<p>PyConf Hyderabad 2024 had 580+ attendees, 35 talks, and dedicated workshops on AI/ML, web development, and open-source contributions. First edition with a scholarship programme.</p>",
        "event_permalink": "pyconf-hyderabad-2024",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Pune —
    {
        "chapter": C["pune"], "event_name": "Pune FOSS Meetup — July 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-07-27 11:00:00", "event_end_date": "2024-07-27 14:00:00",
        "event_location": "Persistent Systems, Pune",
        "event_bio": "July 2024 monthly meetup",
        "event_description": "<p>Talks on open-source ERP adoption in Pune SMEs, Frappe v15 features, and a panel on open-source sustainability funding.</p>",
        "event_permalink": "pune-meetup-jul-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["pune"], "event_name": "PuneFOSS 2024",
        "event_type": "Conference", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-10-05 09:00:00", "event_end_date": "2024-10-05 18:00:00",
        "event_location": "Symbiosis International University, Pune",
        "event_bio": "PuneFOSS 2024 — annual city open-source conference",
        "event_description": "<p>PuneFOSS 2024 attracted 400+ attendees for talks on open-source in manufacturing, ERPNext case studies, and FOSS education. Featured a student project competition.</p>",
        "event_permalink": "punefoss-2024",
        "show_speakers": 1, "show_schedule": 1, "show_cfp": 1, "show_photos": 1, "must_attend": 1,
    },

    # — Kolkata —
    {
        "chapter": C["kolkata"], "event_name": "Kolkata FOSS Meetup — April 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-04-27 11:00:00", "event_end_date": "2024-04-27 14:00:00",
        "event_location": "IEM Campus, EM Bypass, Kolkata",
        "event_bio": "April 2024 monthly meetup",
        "event_description": "<p>Talks on Bengali Wikipedia's 20th anniversary contributions, open-source GIS tools for Kolkata urban planning, and GSoC preparation for students.</p>",
        "event_permalink": "kolkata-meetup-apr-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["kolkata"], "event_name": "Kolkata FOSS Meetup — August 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-08-31 11:00:00", "event_end_date": "2024-08-31 14:00:00",
        "event_location": "Science City, Kolkata",
        "event_bio": "August 2024 monthly meetup",
        "event_description": "<p>Talks on open-source journalism tools, Linux on ARM devices, and a community showcase of FOSS projects from West Bengal.</p>",
        "event_permalink": "kolkata-meetup-aug-2024", "show_photos": 1, "show_rsvp": 1,
    },

    # — Jaipur 2024 (last active events before chapter went inactive) —
    {
        "chapter": C["jaipur"], "event_name": "Jaipur FOSS Meetup — March 2024",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-03-23 11:00:00", "event_end_date": "2024-03-23 14:00:00",
        "event_location": "Manipal University Jaipur",
        "event_bio": "March 2024 meetup in Jaipur",
        "event_description": "<p>Talks on FOSS in Rajasthan tourism sector, open-source tools for artisan communities, and a demo of Kdenlive for video editing.</p>",
        "event_permalink": "jaipur-meetup-mar-2024", "show_photos": 1, "show_rsvp": 1,
    },

    # — FOSS Clubs 2024 —
    {
        "chapter": C["iitb"], "event_name": "IIT Bombay FOSS Club — Install Fest 2024",
        "event_type": "Linux Installation Party", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-08-10 10:00:00", "event_end_date": "2024-08-10 16:00:00",
        "event_location": "Student Activity Centre, IIT Bombay",
        "event_bio": "Annual install fest for incoming students",
        "event_description": "<p>90 students installed Linux in a single day — a new IITB FOSS Club record. Featured a new 'first contribution' track where students made their first open-source PR.</p>",
        "event_permalink": "iitb-install-fest-2024", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["iitb"], "event_name": "IIT Bombay FOSS Club — Open Source Workshop Series",
        "event_type": "Workshop", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-10-05 14:00:00", "event_end_date": "2024-10-05 17:00:00",
        "event_location": "LC201, IIT Bombay",
        "event_bio": "3-session workshop series on contributing to open source",
        "event_description": "<p>Session 1 of 3 in our Hacktoberfest workshop series. This session covered finding good first issues, understanding project structures, and making quality PRs.</p>",
        "event_permalink": "iitb-oss-workshop-oct-2024", "show_rsvp": 1,
    },
    {
        "chapter": C["bits"], "event_name": "BITS Pilani — Open Source Contribution Sprint 2024",
        "event_type": "Hackathon", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-03-23 10:00:00", "event_end_date": "2024-03-24 18:00:00",
        "event_location": "CS Department, BITS Pilani",
        "event_bio": "Weekend contribution sprint",
        "event_description": "<p>40 students spent the weekend contributing to open-source projects. 35 PRs submitted, 22 merged. Top contributor got a FOSS United scholarship.</p>",
        "event_permalink": "bits-sprint-mar-2024", "show_rsvp": 1, "show_photos": 1,
    },
    {
        "chapter": C["nitt"], "event_name": "NIT Trichy FOSS Hackathon 2024",
        "event_type": "Hackathon", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-02-24 09:00:00", "event_end_date": "2024-02-25 18:00:00",
        "event_location": "CS Department, NIT Trichy",
        "event_bio": "Annual open-source hackathon",
        "event_description": "<p>48-hour hackathon with 80 participants. Winning project: an open-source Tamil voice assistant. Runner up: a FOSS alternative to Google Forms built with Frappe.</p>",
        "event_permalink": "nitt-hackathon-2024", "show_rsvp": 1, "show_photos": 1,
    },

    # — Online 2024 —
    {
        "chapter": C["online"], "event_name": "FOSS United Monthly Online Meetup — June 2024",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-06-16 16:00:00", "event_end_date": "2024-06-16 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "June 2024 national online meetup",
        "event_description": "<p>Community updates from all city chapters, a discussion on FOSS United's annual report, and a talk on digital public goods in India.</p>",
        "event_permalink": "online-meetup-jun-2024",
        "show_rsvp": 1,
    },
    {
        "chapter": C["online"], "event_name": "FOSS United Monthly Online Meetup — November 2024",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2024-11-17 16:00:00", "event_end_date": "2024-11-17 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "November 2024 national online meetup",
        "event_description": "<p>Planning session for India FOSS 5.0, community news from city chapters, and a spotlight on new FOSS United member projects.</p>",
        "event_permalink": "online-meetup-nov-2024",
        "show_rsvp": 1,
    },

    # ══════════════════════════════════════════════════════════════════════
    # 2025 — fill months not covered in seed_events.py
    # ══════════════════════════════════════════════════════════════════════

    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — April 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-04-26 10:00:00", "event_end_date": "2025-04-26 13:00:00",
        "event_location": "HasGeek House, Domlur, Bangalore",
        "event_bio": "April 2025 monthly meetup",
        "event_description": "<p>Talks on eBPF, open-source observability, and a demo of GNOME 48 new features.</p>",
        "event_permalink": "blr-meetup-apr-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — July 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-07-26 10:00:00", "event_end_date": "2025-07-26 13:00:00",
        "event_location": "91springboard, Koramangala, Bangalore",
        "event_bio": "July 2025 monthly meetup — post India FOSS edition",
        "event_description": "<p>Post India FOSS 4.0 community debrief, talk highlights, and planning for BangaloreFOSS 2025.</p>",
        "event_permalink": "blr-meetup-jul-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["bangalore"], "event_name": "Bengaluru FOSS Meetup — October 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-10-25 10:00:00", "event_end_date": "2025-10-25 13:00:00",
        "event_location": "NIMHANS Convention Centre, Bangalore",
        "event_bio": "October 2025 Hacktoberfest meetup",
        "event_description": "<p>Hacktoberfest 2025 community meetup with live contribution sessions, mentorship from experienced contributors, and project demos.</p>",
        "event_permalink": "blr-meetup-oct-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — June 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-06-28 11:00:00", "event_end_date": "2025-06-28 14:00:00",
        "event_location": "Maker's Asylum, Andheri, Mumbai",
        "event_bio": "June 2025 monthly meetup",
        "event_description": "<p>Talks on open-source hardware, RISC-V adoption, and open-source accessibility tools for persons with disabilities.</p>",
        "event_permalink": "mumbai-meetup-jun-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["mumbai"], "event_name": "Mumbai FOSS Meetup — October 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-10-25 11:00:00", "event_end_date": "2025-10-25 14:00:00",
        "event_location": "Bombay Connect, Andheri East, Mumbai",
        "event_bio": "October 2025 monthly meetup",
        "event_description": "<p>Talks on open-source fintech tools, a panel on women in FOSS, and a community project showcase.</p>",
        "event_permalink": "mumbai-meetup-oct-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Meetup — July 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-07-26 11:00:00", "event_end_date": "2025-07-26 14:00:00",
        "event_location": "IIT Delhi, Hauz Khas",
        "event_bio": "July 2025 monthly meetup",
        "event_description": "<p>India FOSS 4.0 speaker recap, talks on open data in India, and planning for Delhi chapter events in Q3–Q4 2025.</p>",
        "event_permalink": "delhi-meetup-jul-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["delhi"], "event_name": "Delhi FOSS Meetup — October 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-10-18 11:00:00", "event_end_date": "2025-10-18 14:00:00",
        "event_location": "Delhivery HQ, Gurugram",
        "event_bio": "October 2025 monthly meetup",
        "event_description": "<p>Talks on FOSS in the Indian public sector, open-source in smart cities, and Hacktoberfest retrospective.</p>",
        "event_permalink": "delhi-meetup-oct-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Meetup — May 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-05-31 10:00:00", "event_end_date": "2025-05-31 13:00:00",
        "event_location": "IIT Madras Research Park, Chennai",
        "event_bio": "May 2025 monthly meetup",
        "event_description": "<p>Talks on Tamil NLP with open-source LLMs, FOSS tools for the publishing industry, and a community GSoC celebration.</p>",
        "event_permalink": "chennai-meetup-may-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["chennai"], "event_name": "Chennai FOSS Meetup — September 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-09-27 10:00:00", "event_end_date": "2025-09-27 13:00:00",
        "event_location": "Anna University, Guindy, Chennai",
        "event_bio": "September 2025 monthly meetup",
        "event_description": "<p>Talks on open-source AI voice models for Tamil, LibreOffice Impress new features, and a panel on FOSS in Tamil Nadu government digital initiatives.</p>",
        "event_permalink": "chennai-meetup-sep-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Meetup — May 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-05-31 11:00:00", "event_end_date": "2025-05-31 14:00:00",
        "event_location": "T-Hub, Raidurgam, Hyderabad",
        "event_bio": "May 2025 monthly meetup",
        "event_description": "<p>Talks on open-source generative AI tools, contributing to Zulip, and a student project showcase from IIIT Hyderabad.</p>",
        "event_permalink": "hyd-meetup-may-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["hyderabad"], "event_name": "Hyderabad FOSS Meetup — October 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-10-25 11:00:00", "event_end_date": "2025-10-25 14:00:00",
        "event_location": "IIIT Hyderabad, Gachibowli",
        "event_bio": "October 2025 monthly meetup",
        "event_description": "<p>Talks on KDE Plasma 6.2, open-source robotics, and Hacktoberfest 2025 contribution session.</p>",
        "event_permalink": "hyd-meetup-oct-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["pune"], "event_name": "Pune FOSS Meetup — June 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-06-28 11:00:00", "event_end_date": "2025-06-28 14:00:00",
        "event_location": "CoWork Cafe, Kothrud, Pune",
        "event_bio": "June 2025 monthly meetup",
        "event_description": "<p>Talks on open-source ERP for manufacturing, Frappe Cloud internals, and a community project showcase.</p>",
        "event_permalink": "pune-meetup-jun-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["pune"], "event_name": "Pune FOSS Meetup — October 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-10-25 11:00:00", "event_end_date": "2025-10-25 14:00:00",
        "event_location": "Persistent Systems, Pune",
        "event_bio": "October 2025 monthly meetup",
        "event_description": "<p>Talks on open-source supply chain security (SBOM), Frappe 15 LTS release, and Hacktoberfest contribution walkthrough.</p>",
        "event_permalink": "pune-meetup-oct-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["kolkata"], "event_name": "Kolkata FOSS Meetup — May 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-05-31 11:00:00", "event_end_date": "2025-05-31 14:00:00",
        "event_location": "Webel Bhavan, Salt Lake, Kolkata",
        "event_bio": "May 2025 monthly meetup",
        "event_description": "<p>Talks on open-source tools for Bengali literature digitization, Linux for artists, and student contributor spotlights.</p>",
        "event_permalink": "kolkata-meetup-may-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["kolkata"], "event_name": "Kolkata FOSS Meetup — August 2025",
        "event_type": "Meet Up", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-08-30 11:00:00", "event_end_date": "2025-08-30 14:00:00",
        "event_location": "Science City, Kolkata",
        "event_bio": "August 2025 monthly meetup",
        "event_description": "<p>Post India FOSS 4.0 community debrief, talks on open-source data science tools, and planning for KolkatFOSS 2026.</p>",
        "event_permalink": "kolkata-meetup-aug-2025", "show_photos": 1, "show_rsvp": 1,
    },
    {
        "chapter": C["online"], "event_name": "FOSS United Monthly Online Meetup — May 2025",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-05-18 16:00:00", "event_end_date": "2025-05-18 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "May 2025 national online meetup",
        "event_description": "<p>Community updates, India FOSS 4.0 CFP countdown, and a talk on open-source AI tools that respect user privacy.</p>",
        "event_permalink": "online-meetup-may-2025", "show_rsvp": 1,
    },
    {
        "chapter": C["online"], "event_name": "FOSS United Monthly Online Meetup — October 2025",
        "event_type": "Online", "status": "Concluded", "is_published": 1,
        "event_start_date": "2025-10-19 16:00:00", "event_end_date": "2025-10-19 18:00:00",
        "event_location": "Online (Jitsi Meet)",
        "event_bio": "October 2025 national online meetup",
        "event_description": "<p>Chapter updates, India FOSS 5.0 early planning discussions, and a talk on FOSS in Indian healthcare.</p>",
        "event_permalink": "online-meetup-oct-2025", "show_rsvp": 1,
    },
]


def create_events():
    valid_fields = {f.fieldname for f in frappe.get_meta("FOSS Chapter Event").fields}
    created = skipped = 0

    for data in EVENTS:
        permalink = data.get("event_permalink")
        if frappe.db.exists("FOSS Chapter Event", {"event_permalink": permalink}):
            print(f"  SKIP  {data['event_name'][:65]}")
            skipped += 1
            continue

        clean = {k: v for k, v in data.items() if k in valid_fields or k == "doctype"}
        clean["doctype"] = "FOSS Chapter Event"

        doc = frappe.get_doc(clean)
        doc.insert(ignore_permissions=True)
        year = doc.event_start_date[:4]
        print(f"  {year} | {doc.status:10s} | {doc.event_type:25s} | {doc.event_name[:50]}")
        created += 1

    frappe.db.commit()
    print(f"\nDone — {created} created, {skipped} skipped.")
