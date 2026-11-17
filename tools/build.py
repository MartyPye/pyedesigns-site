import os, sys
OUT = sys.argv[1]
EMAIL = "support@pyedesigns.com"
LEGAL = "Pye Designs LLC"
COMPANY = "Pye Designs"
YEAR = "2026"
DOMAIN = "itspyedesign.com"

def page(path, title, desc, current, body):
    depth = path.count("/")
    root = "/" if path == "404.html" else ("../" if path else "")
    def nav(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{root}{href}"{cur}>{label}</a>'
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{root}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{root}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{root}assets/site.css">
</head>
<body>
<header class="site"><div class="wrap">
<a class="brand" href="{root}"><img src="{root}assets/mark.svg" alt=""><span>{COMPANY}</span></a>
<nav class="main" aria-label="Main">{nav("swingjournal/","SwingJournal","app")}{nav("support/","Support","support")}{nav("privacy/","Privacy","privacy")}</nav>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap">
<div>&copy; {YEAR} {LEGAL}. All rights reserved.</div>
<nav aria-label="Footer"><a href="{root}swingjournal/">SwingJournal</a><a href="{root}support/">Support</a><a href="{root}privacy/">Privacy policy</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
</div></footer>
</body>
</html>
"""
    full = os.path.join(OUT, path, "index.html") if path else os.path.join(OUT, "index.html")
    if path.endswith(".html"):
        full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w").write(html)

home = f"""
<div class="eyebrow">Software studio</div>
<h1>Small, focused software for the things you care about.</h1>
<p class="lede">{COMPANY} designs and builds niche apps for Apple platforms. We pick one problem, make a tool that does it well, and keep your data yours.</p>

<div class="card product">
  <img src="assets/swingjournal-icon.png" alt="SwingJournal app icon">
  <div>
    <h2>SwingJournal</h2>
    <p>A private tennis journal for iPhone and iPad. Prep before you play, review after, and know every opponent.</p>
    <div class="actions"><a class="btn" href="swingjournal/">Learn more</a><a class="btn ghost" href="support/">Support</a></div>
  </div>
</div>

<h2>About {COMPANY}</h2>
<div class="prose">
<p>{LEGAL} is an independent software company. We build apps for people with a specific need that general-purpose tools don't quite meet, starting with competitive tennis players who want to remember what works.</p>
<p>Our apps are native, quiet and private by default. No accounts, no ads, no tracking. Your data lives on your devices and in your own iCloud.</p>
</div>

<h2>Contact</h2>
<div class="card">
<dl class="contact">
  <dt>Company</dt><dd>{LEGAL}</dd>
  <dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
  <dt>Web</dt><dd>{DOMAIN}</dd>
</dl>
</div>
"""
page("", f"{COMPANY}", f"{COMPANY} makes small, focused, private apps for iPhone and iPad, including SwingJournal, a tennis journal.", "home", home)

feats = [
 ("Know every opponent", "Search a name and see your head-to-head, every match and score, their strengths, weaknesses and rating."),
 ("Prep before you play", "Plan A and Plan B, serve and return strategy, cue words and a warm-up, with what you already know about your opponent."),
 ("Review after", "How the plan worked, what went well, what to improve and the lessons to carry into the next match."),
 ("Structured practice", "Objectives, drills from your own library and a rating for each drill, so practice has a point."),
 ("Quick notes at the court", "Jot a note or record a voice memo between sets, then write the full review at home."),
 ("Private by design", "No account and no servers. Your journal stays on your devices and syncs through your own iCloud."),
]
fhtml = "".join(f'<div class="card"><h3>{t}</h3><p>{d}</p></div>' for t, d in feats)
app = f"""
<div class="hero-app">
  <img src="../assets/swingjournal-icon.png" alt="SwingJournal app icon">
  <div class="eyebrow">For iPhone and iPad</div>
  <h1>SwingJournal</h1>
  <p class="lede">Your private tennis journal. Players, matches and practices, with prep before and review after.</p>
  <span class="pill">Coming soon to the App Store</span>
</div>

<div class="grid features">{fhtml}</div>

<h2>Pricing</h2>
<p class="muted">Every new journal starts with a free 14-day trial of everything. After that, keep using SwingJournal for free with up to 10 players and 5 sessions, or subscribe to SwingJournal Pro for no limits.</p>
<div class="grid prices">
  <div class="card"><div class="muted">Monthly</div><div class="price">$4.99</div><div class="small">per month</div></div>
  <div class="card"><div class="muted">Yearly</div><div class="price">$44.99</div><div class="small">per year, save 25%</div></div>
</div>
<p class="small" style="margin-top:14px">Subscriptions are billed through your Apple Account and renew automatically unless cancelled at least 24 hours before the end of the period. Manage or cancel them in Settings &gt; [your name] &gt; Subscriptions. Even without a subscription, you can always view, edit and export what you've already written. Available in the United States, in English. Requires iOS 18 or later.</p>

<div class="actions" style="margin-top:28px"><a class="btn" href="../support/">Get support</a><a class="btn ghost" href="../privacy/">Privacy policy</a></div>
"""
page("swingjournal", "SwingJournal, a private tennis journal", "SwingJournal is a private tennis journal for iPhone and iPad by Pye Designs: know every opponent, prep before you play and review after.", "app", app)

faqs = [
 ("Where is my journal stored?", "On your device, and in your own private iCloud if you're signed in, so it syncs between your iPhone and iPad. We can't see it."),
 ("How do I move my journal to a new iPhone?", "Sign in to the same Apple Account with iCloud turned on for SwingJournal. Your journal syncs down on its own."),
 ("How do I cancel my subscription?", "Open Settings on your iPhone, tap your name, then Subscriptions, and choose SwingJournal. Apple handles all billing."),
 ("I subscribed but the app still shows the free limits.", "In SwingJournal, go to Settings and tap Restore purchases. Make sure you're signed in with the Apple Account you used to subscribe."),
 ("Can I get my data out?", "Yes. In SwingJournal's Settings, choose Export as JSON or Export as CSV. Export always works, with or without a subscription."),
]
qhtml = "".join(f"<h3>{q}</h3><p class='muted'>{a}</p>" for q, a in faqs)
support = f"""
<div class="eyebrow">Support</div>
<h1>How can we help?</h1>
<p class="lede">Questions, bugs or ideas for SwingJournal? Email us and a real person will reply, usually within two business days.</p>
<div class="actions" style="margin:8px 0 8px"><a class="btn" href="mailto:{EMAIL}?subject=SwingJournal%20support">Email {EMAIL}</a></div>
<p class="small">It helps to include your device, iOS version and the app version (you can find it in SwingJournal's Settings).</p>

<h2>Common questions</h2>
<div class="card prose" style="max-width:none">{qhtml}</div>
"""
page("support", f"Support, {COMPANY}", f"Get help with SwingJournal and contact {COMPANY}.", "support", support)

privacy = f"""
<div class="prose">
<div class="eyebrow">Privacy policy</div>
<h1>Your data stays with you</h1>
<p class="small">Effective November 17, 2026</p>
<p>This policy covers SwingJournal, the tennis journal app made by {LEGAL} ("{COMPANY}", "we"), and this website. The short version: we don't collect anything.</p>

<h2>SwingJournal</h2>
<h3>What we collect</h3>
<p>Nothing. SwingJournal has no account, no server, no analytics and no advertising. {COMPANY} never receives your journal, your players, your notes or anything about how you use the app.</p>
<h3>Where your journal is stored</h3>
<p>Everything you enter (players, photos, matches, practices, notes, voice memos and reviews) is stored on your device. If you're signed in to iCloud, it's also kept in your own private iCloud database so it syncs to your other iPhone and iPad. Only your Apple Account can read that database; {COMPANY} can't. <a href="https://www.apple.com/legal/privacy/">Apple's privacy policy</a> covers iCloud.</p>
<p>If iCloud is off, your journal stays on that device only.</p>
<h3>Contacts and photos</h3>
<p>When you add a player from Contacts or link a contact, you pick one card in Apple's contact picker, and SwingJournal saves only that card's name, phone number and photo with the player. The app never reads the rest of your contacts and doesn't ask for Contacts access. Photos you choose for players are saved with your journal in the same way.</p>
<h3>Microphone and speech recognition</h3>
<p>If you record a voice memo, SwingJournal asks for the microphone. Recordings are saved with your journal as described above. Turning a memo into text happens on your device; the audio isn't sent anywhere to be transcribed.</p>
<h3>Notifications</h3>
<p>Review reminders are scheduled on your device. Nothing is sent to us to deliver them.</p>
<h3>Purchases</h3>
<p>Subscriptions are handled by Apple through the App Store. {COMPANY} doesn't see your payment details; the app only learns whether your subscription is active.</p>
<h3>Exports</h3>
<p>When you export your journal as JSON or CSV, the file goes wherever you choose to share or save it. That's up to you.</p>
<h3>Children</h3>
<p>SwingJournal is meant for players of all ages, including juniors, and collects no data from anyone.</p>
<h3>Deleting your data</h3>
<p>Delete players or sessions in the app, or delete the app. To remove the iCloud copy, go to Settings &gt; [your name] &gt; iCloud &gt; Manage Account Storage and delete SwingJournal's data.</p>

<h2>This website</h2>
<p>This website has no cookies, analytics, ads or forms. Like any web host, our hosting provider may keep standard server logs (such as IP address and browser type) for security and reliability. We don't use them to identify you. If you email us, we use your message and address only to reply.</p>

<h2>Changes and contact</h2>
<p>If this policy changes, the new version will be posted on this page with a new effective date. Questions: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>
"""
page("privacy", f"Privacy policy, {COMPANY}", f"Privacy policy for SwingJournal and the {COMPANY} website.", "privacy", privacy)

nf = """<div class="eyebrow">404</div><h1>Page not found</h1><p class="lede">That page doesn't exist. Try the <a href="/">home page</a>.</p>"""
page("404.html", f"Page not found, {COMPANY}", "Page not found.", "", nf)
open(os.path.join(OUT, "CNAME"), "w").write(DOMAIN + "\n")
