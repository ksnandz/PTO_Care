import tkinter as tk
import webbrowser

text = tk.StringVar


def raise_frame(frame):
    frame.tkraise()


def callback(url):
    webbrowser.open_new(url)


# INITIATING GUI
root = tk.Tk()
root.title("PTO_Care")
root.geometry("700x600")

f_helpful = tk.Frame(root)
f_helpline = tk.Frame(root)
f_general = tk.Frame(root)
f_consultation = tk.Frame(root)
f_guide1_breathing = tk.Frame(root)
f_guide1_back_pain = tk.Frame(root)
f_guide1_chest_pain = tk.Frame(root)
f_transport1 = tk.Frame(root)
f_transport2 = tk.Frame(root)
f_transport_Scar = tk.Frame(root)
f_transport_Bram = tk.Frame(root)
f_guide1 = tk.Frame(root)
f1 = tk.Frame(root)

f_helpful.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_helpline.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_general.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_consultation.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_guide1_breathing.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_guide1_back_pain.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_guide1_chest_pain.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_transport_Bram.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_transport_Scar.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_transport2.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_transport1.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f_guide1.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")
f1.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor="n")

# TYPE OF REQUEST
text_box1 = tk.Label(f1, text="What kind of service are you looking for?", font=("arial", 20, "bold"))
text_box1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.12)
button_11 = tk.Button(f1, text="Transportation", command=lambda: raise_frame(f_transport1))
button_11.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.15)
button_12 = tk.Button(f1, text="Consultation", command=lambda: raise_frame(f_consultation))
button_12.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.15)
button_13 = tk.Button(f1, text="Post Treatment Guidelines", command=lambda: raise_frame(f_guide1))
button_13.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.15)
button_14 = tk.Button(f1, text="Helpful Tips", command=lambda: raise_frame(f_helpful))
button_14.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.15)

# INJURY
text_box_guide1 = tk.Label(f_guide1, text="Why did you go to the ER?", font=("arial", 20, "bold"))
text_box_guide1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.12)
button_guide1 = tk.Button(f_guide1, text="Chest Pain", command=lambda: raise_frame(f_guide1_chest_pain))
button_guide1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.08)
button_guide2 = tk.Button(f_guide1, text="Back Injury/Pain", command=lambda: raise_frame(f_guide1_back_pain))
button_guide2.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.08)
button_guide3 = tk.Button(f_guide1, text="Breathing Difficulties", command=lambda: raise_frame(f_guide1_breathing))
button_guide3.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.08)
button_guide4 = tk.Button(f_guide1, text="Sinus Infection")
button_guide4.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.08)
button_guide5 = tk.Button(f_guide1, text="Injuries & Accidents")
button_guide5.place(relx=0.2, rely=0.5, relwidth=0.6, relheight=0.08)
button_guide6 = tk.Button(f_guide1, text="Abdominal Pain")
button_guide6.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.08)
button_guide7 = tk.Button(f_guide1, text="Traumatic Head Injury")
button_guide7.place(relx=0.2, rely=0.7, relwidth=0.6, relheight=0.08)

# FINAL GUIDELINES
# CHEST PAIN
text_box_guide1_chest_pain = tk.Label(f_guide1_chest_pain, text="Recommended Actions/Advice",
                                      font=("arial", 20, "bold"))
text_box_guide1_chest_pain.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.15)
text_box_guide1_chest_pain1 = tk.Label(f_guide1_chest_pain, text="Aspirin - take aspirin if the pain is related to\n "
                                                                 "your heart", font=("arial", 15))
text_box_guide1_chest_pain1.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.12)
text_box_guide1_chest_pain2 = tk.Label(f_guide1_chest_pain, text="Lie Down - If recurring pain occurs, lying down\n "
                                                                 "immediately with the head elevated above the\n "
                                                                 "body may bring some relief. A slightly upright\n "
                                                                 "position helps when the pain is due to reflux.",
                                       font=("arial", 15))
text_box_guide1_chest_pain2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.14)
text_box_guide1_chest_pain3 = tk.Label(f_guide1_chest_pain, text="Antidepressants - Suggested if experiencing panic\n "
                                                                 "attacks to control symptoms. Cognitive behavioural\n "
                                                                 "therapy may be applicable", font=("arial", 15))
text_box_guide1_chest_pain3.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.14)
text_box_guide1_chest_pain4 = tk.Label(f_guide1_chest_pain, text="Recommended Foods", font=("arial", 20, "bold"))
text_box_guide1_chest_pain4.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.15)
text_box_guide1_chest_pain5 = tk.Label(f_guide1_chest_pain, text="Almonds, Hot Drinks, Garlic", font=("arial", 15))
text_box_guide1_chest_pain5.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.12)

# BACK PAIN
text_box_guide1_back_pain = tk.Label(f_guide1_back_pain, text="Recommended Actions/Advice",
                                     font=("arial", 20, "bold"))
text_box_guide1_back_pain.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
text_box_guide1_back_pain1 = tk.Label(f_guide1_back_pain, text="Physical Activity - Reduce physical activity for a\n "
                                                               "few days. Calms symptoms and swelling if applicable",
                                      font=("arial", 15))
text_box_guide1_back_pain1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.14)
text_box_guide1_back_pain2 = tk.Label(f_guide1_back_pain, text="Ice/Heat - Apply ice to the painful area for the\n "
                                                               "first 48-72 hours, then use heat.",
                                      font=("arial", 15))
text_box_guide1_back_pain2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.12)
text_box_guide1_back_pain3 = tk.Label(f_guide1_back_pain, text="Painkillers - Ibuprofen such as Advil, Motrin IB or\n "
                                                               "acetaminophen like Tylenol are suggested",
                                      font=("arial", 15))
text_box_guide1_back_pain3.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.12)
text_box_guide1_back_pain4 = tk.Label(f_guide1_back_pain, text="To Avoid", font=("arial", 20, "bold"))
text_box_guide1_back_pain4.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.15)
text_box_guide1_back_pain5 = tk.Label(f_guide1_back_pain, text="Heavy, lifting, or twisting of your back for 6 weeks\n "
                                                               "prior to pain", font=("arial", 15))
text_box_guide1_back_pain5.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.12)
text_box_guide1_back_pain5 = tk.Label(f_guide1_back_pain, text="No exercise for a week after the pain began. Visit a\n "
                                                               "physical therapist for exercising after 2-3 weeks",
                                      font=("arial", 15))
text_box_guide1_back_pain5.place(relx=0.1, rely=0.7, relwidth=0.8, relheight=0.12)

# BREATHING
text_box_guide1_breathing = tk.Label(f_guide1_breathing, text="Recommended Actions/Advice",
                                     font=("arial", 20, "bold"))
text_box_guide1_breathing.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
text_box_guide1_breathing1 = tk.Label(f_guide1_breathing, text="Posture - Leaning forwards with your arms on the "
                                                               "table\n "
                                                               " to potentially facilitate breathing",
                                      font=("arial", 15))
text_box_guide1_breathing1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.14)
text_box_guide1_breathing2 = tk.Label(f_guide1_breathing, text="Posture - Standing against the wall to support your\n "
                                                               "back",
                                      font=("arial", 15))
text_box_guide1_breathing2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.12)
text_box_guide1_breathing3 = tk.Label(f_guide1_breathing, text="Breathing method - Diaphragmatic breathing:\n\n 1. Sit "
                                                               "in a chair with bent knees and relax shoulders, head, "
                                                               "and neck\n\n2. Breath in slowly through your "
                                                               "nose\n\n3. As "
                                                               "you exhale, tighten your muscles\n\n4. Put more "
                                                               "emphasis "
                                                               "on the exhale rather than inhale\n\n5. Repeat for "
                                                               "about "
                                                               "5 "
                                                               "minutes",
                                      font=("arial", 15))
text_box_guide1_breathing3.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.44)

# CONSULTATION
text_box_consultation = tk.Label(f_consultation, text="Select an Option", font=("arial", 20, "bold"))
text_box_consultation.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.12)
button_2 = tk.Button(f_consultation, text="Helplines", command=lambda: raise_frame(f_helpline))
button_2.place(relx=0.2, rely=0.375, relwidth=0.6, relheight=0.2)

# GENERAL
text_box_general1 = tk.Label(f_helpful, text="Listen to Your Body", font=("arial", 20, "bold"))
text_box_general1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.12)
text_box_general2 = tk.Label(f_helpful, text="It can be easy to shrug off symptoms of depression\n or anxiety after an "
                                             "event like that, \nbecause it seems “normal” to feel that way when\n "
                                             "you’ve "
                                             "been through a traumatic experience.\n But it’s important to notice the "
                                             "ways you’re not\n feeling like yourself. (Ex. feeling anxious/angry,\n "
                                             "having trouble concentrating, not being\n able to stop thinking about "
                                             "your injury).", font=("arial", 15))
text_box_general2.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.4)
text_box_general3 = tk.Label(f_helpful, text="Possible Treatments", font=("arial", 20, "bold"))
text_box_general3.place(relx=0.1, rely=0.45, relwidth=0.8, relheight=0.12)
text_box_general4 = tk.Label(f_helpful, text="- Treatments include psychotherapy, cognitive behaviour therapy,\n "
                                             "antidepressants, meditation, and attending support groups with others\n "
                                             "going through injury recovery.", font=("arial", 15))
text_box_general4.place(relx=0.1, rely=0.55, relwidth=0.8, relheight=0.1)
text_box_general5 = tk.Label(f_helpful, text="- Prevent alcohol and drugs", font=("arial", 15))
text_box_general5.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.1)


# HELPLINE
link_helpline1 = tk.Label(f_helpline, text="Camh (The Centre of Addiction & Mental Health)\n 1‑877‑225‑2212",
                          fg="blue", cursor="hand2")
link_helpline1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
link_helpline1.bind("<Button-1>", lambda e: callback("https://www.camh.ca"))

link_helpline2 = tk.Label(f_helpline, text="Hope for Wellness Helpline\n 1-855-242-3310",
                          fg="blue", cursor="hand2")
link_helpline2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.15)
link_helpline2.bind("<Button-1>", lambda e: callback("https://www.hopeforwellness.ca"))

link_helpline3 = tk.Label(f_helpline, text="Crisis Services Canada\n 1-833-456-4566",
                          fg="blue", cursor="hand2")
link_helpline3.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.15)
link_helpline3.bind("<Button-1>", lambda e: callback("https://www.crisisservicescanada.ca/en/"))

# REGION
text_box_tran1 = tk.Label(f_transport1, text="Select a region", font=("arial", 20, "bold"))
text_box_tran1.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.12)
button_T11 = tk.Button(f_transport1, text="Greater Toronto Area (GTA)", command=lambda: raise_frame(f_transport2))
button_T11.place(relx=0.2, rely=0.15, relwidth=0.6, relheight=0.1)
button_T12 = tk.Button(f_transport1, text="Ottawa Region")
button_T12.place(relx=0.2, rely=0.275, relwidth=0.6, relheight=0.1)
button_T13 = tk.Button(f_transport1, text="Niagara Region")
button_T13.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)
button_T14 = tk.Button(f_transport1, text="Durham Region")
button_T14.place(relx=0.2, rely=0.525, relwidth=0.6, relheight=0.1)
button_T14 = tk.Button(f_transport1, text="Waterloo Region")
button_T14.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.1)
button_T15 = tk.Button(f_transport1, text="Oxford County")
button_T15.place(relx=0.2, rely=0.775, relwidth=0.6, relheight=0.1)
button_T16 = tk.Button(f_transport1, text="Go back to the previous page", command=lambda: raise_frame(f1))
button_T16.place(relx=0.2, rely=0.9, relwidth=0.6, relheight=0.1)

# CITY
text_box_tran2 = tk.Label(f_transport2, text="Select a city", font=("arial", 20, "bold"))
text_box_tran2.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.12)
button_T21 = tk.Button(f_transport2, text="Scarborough", command=lambda: raise_frame(f_transport_Scar))
button_T21.place(relx=0.2, rely=0.15, relwidth=0.6, relheight=0.1)
button_T22 = tk.Button(f_transport2, text="Brampton", command=lambda: raise_frame(f_transport_Bram))
button_T22.place(relx=0.2, rely=0.275, relwidth=0.6, relheight=0.1)
button_T23 = tk.Button(f_transport2, text="Mississauga")
button_T23.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)
button_T24 = tk.Button(f_transport2, text="Downtown Toronto")
button_T24.place(relx=0.2, rely=0.525, relwidth=0.6, relheight=0.1)
button_T24 = tk.Button(f_transport2, text="Markham")
button_T24.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.1)
button_T25 = tk.Button(f_transport2, text="York")
button_T25.place(relx=0.2, rely=0.775, relwidth=0.6, relheight=0.1)
button_T26 = tk.Button(f_transport2, text="Go back to the previous page", command=lambda: raise_frame(f_transport1))
button_T26.place(relx=0.2, rely=0.9, relwidth=0.6, relheight=0.1)

# FINAL TRANSPORT
link_Scar1 = tk.Label(f_transport_Scar, text="Wheelchair Accessible Transit\n  TEL:416‑884‑9898 | 1‑877‑225‑2212",
                      fg="blue", cursor="hand2")
link_Scar1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
link_Scar1.bind("<Button-1>", lambda e: callback("https://www.wheelchairtransit.com/wheelchair/"))
link_Scar2 = tk.Label(f_transport_Scar, text="King Transit\n  TEL:416-208-3404", fg="blue", cursor="hand2")
link_Scar2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.15)
link_Scar2.bind("<Button-1>", lambda e: callback("https://www.kingtransit.com"))
link_Scar3 = tk.Label(f_transport_Scar, text="RNR Patient Transfer Service\n  TEL:705-327-0070",
                      fg="blue", cursor="hand2")
link_Scar3.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.15)
link_Scar3.bind("<Button-1>", lambda e: callback("http://rnrpt.com/services/specialty-transfers/wheelchair-transfers/"))
back_Scar = tk.Button(f_transport_Scar, text="Go back to the previous page", command=lambda: raise_frame(f_transport2))
back_Scar.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)

link_Bram1 = tk.Label(f_transport_Bram, text="Caledon Community Services Transportation\n TEL:905-951-2300 | "
                                             "905-584-2300", fg="blue", cursor="hand2")
link_Bram1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)
link_Bram1.bind("<Button-1>", lambda e: callback("https://www.ccs4u.org"))
link_Bram2 = tk.Label(f_transport_Bram, text="CANES Community Care\n  TEL:416-743-38921-877-7433-025",
                      fg="blue", cursor="hand2")
link_Bram2.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.15)
link_Bram2.bind("<Button-1>", lambda e: callback("https://www.canes.on.ca"))
link_Bram3 = tk.Label(f_transport_Bram, text="Dignity Transportation Inc\n  TEL:416-398-2222 | "
                                             "1-866-398-2109", fg="blue", cursor="hand2")
link_Bram3.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.15)
link_Bram3.bind("<Button-1>", lambda e: callback("http://www.dignitytransportation.com/"))

back_Bram = tk.Button(f_transport_Bram, text="Go back to the previous page", command=lambda: raise_frame(f_transport2))
back_Bram.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)

back_guide1 = tk.Button(f_guide1, text="Go back to the previous page", command=lambda: raise_frame(f1))
back_guide1.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)

back_chest_pain = tk.Button(f_guide1_chest_pain, text="Go back to the previous page",
                            command=lambda: raise_frame(f_guide1))
back_chest_pain.place(relx=0.2, rely=0.9, relwidth=0.6, relheight=0.1)

back_back_pain = tk.Button(f_guide1_back_pain, text="Go back to the previous page",
                           command=lambda: raise_frame(f_guide1))
back_back_pain.place(relx=0.2, rely=0.85, relwidth=0.6, relheight=0.1)

back_breathing = tk.Button(f_guide1_breathing, text="Go back to the previous page",
                           command=lambda: raise_frame(f_guide1))
back_breathing.place(relx=0.2, rely=0.85, relwidth=0.6, relheight=0.1)

back_consultation = tk.Button(f_consultation, text="Go back to the previous page", command=lambda: raise_frame(f1))
back_consultation.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)

back_helpline = tk.Button(f_helpline, text="Go back to the previous page",
                          command=lambda: raise_frame(f_consultation))
back_helpline.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)

back_general = tk.Button(f_general, text="Go back to the previous page",
                         command=lambda: raise_frame(f_consultation))
back_general.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)

back_helpful = tk.Button(f_helpful, text="Go back to the previous page", command=lambda: raise_frame(f1))
back_helpful.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.1)
#

root.mainloop()
