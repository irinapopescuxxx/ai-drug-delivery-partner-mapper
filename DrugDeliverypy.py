import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Drug Delivery Partner Mapper", page_icon="🤝", layout="wide")

# ---- Hera-style CSS ----
st.markdown(
    """
    <style>
      .block-container { padding-top: 2rem; padding-bottom: 2.5rem; }

      .hera-hero h1 {
        font-size: 3.0rem;
        line-height: 1.05;
        margin-bottom: 0.25rem;
        letter-spacing: 0.2px;
      }
      .hera-sub {
        font-size: 1.05rem;
        opacity: 0.9;
        margin-top: 0.25rem;
        margin-bottom: 1.25rem;
      }

      div.stButton > button,
      div.stDownloadButton > button {
        border-radius: 999px !important;
        padding: 0.6rem 1.1rem !important;
        border: 1px solid rgba(127,182,255,0.45) !important;
      }

      [data-testid="stDataFrame"] {
        border-radius: 14px;
        overflow: hidden;
      }

      [data-testid="stMetric"] {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 14px;
        padding: 12px 14px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- Hera-style header ----
left, right = st.columns([1.2, 3])

with left:
    st.markdown("### HERA HEALTH SOLUTIONS")


st.markdown("---")

# ---- Hero section ----
st.markdown(
    """
    <div class="hera-hero">
      <h1>AI Partner Mapper</h1>
      <div class="hera-sub">
        Identify and compare AI partners in drug discovery and delivery, optimized for Hera-style priorities.
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
# -----------------------------
# 1) Starter dataset (edit/expand)
# -----------------------------
# COPY-PASTE REPLACEMENT for your STARTER_COMPANIES list
# This is the SAME list you already have, but with "Trend Tags" added to EVERY company.
# Paste this whole block over your existing STARTER_COMPANIES = [ ... ] section.

STARTER_COMPANIES = [
    {
        "Company": "Recursion",
        "Type": "Public company",
        "Primary Focus": "Drug discovery",
        "AI Methods": "Computer vision, ML on high-throughput biology",
        "Therapeutic Areas": "Broad",
        "Delivery Relevance (0-5)": 1,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 3,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "automation, high-throughput screening, computer vision, phenotypic screening",
        "Notes": "Strong discovery platform, lower direct delivery alignment."
    },
    {
        "Company": "Insilico Medicine",
        "Type": "Private company",
        "Primary Focus": "Drug discovery",
        "AI Methods": "Generative models, target ID, molecule design",
        "Therapeutic Areas": "Multiple",
        "Delivery Relevance (0-5)": 1,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 3,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "generative AI, target identification, molecule design, predictive modeling",
        "Notes": "Good AI discovery partner, not delivery-focused."
    },
    {
        "Company": "Exscientia",
        "Type": "Public company",
        "Primary Focus": "Drug discovery",
        "AI Methods": "ML-guided design, automated experimentation",
        "Therapeutic Areas": "Oncology, immunology",
        "Delivery Relevance (0-5)": 1,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 3,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "generative AI, automation, ML-guided design, active learning",
        "Notes": "Discovery partner potential, limited delivery fit."
    },
    {
        "Company": "Schrödinger",
        "Type": "Public company",
        "Primary Focus": "Computational modeling",
        "AI Methods": "Physics-based simulation + ML",
        "Therapeutic Areas": "Broad",
        "Delivery Relevance (0-5)": 2,
        "Implant Fit (0-5)": 2,
        "Clinical Stage Strength (0-5)": 2,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "molecular simulation, predictive modeling, physics-based modeling, digital twin",
        "Notes": "Strong modeling; could support formulation or material modeling indirectly."
    },
    {
        "Company": "Moderna",
        "Type": "Big pharma",
        "Primary Focus": "Drug delivery",
        "AI Methods": "Optimization, analytics, automation",
        "Therapeutic Areas": "Vaccines, mRNA",
        "Delivery Relevance (0-5)": 4,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 5,
        "Partnership Openness (0-5)": 2,
        "Trend Tags": "drug delivery, lipid nanoparticles, mRNA, manufacturing, optimization",
        "Notes": "Delivery expertise, but platform focus differs from implants."
    },
    {
        "Company": "Pfizer",
        "Type": "Big pharma",
        "Primary Focus": "Drug development",
        "AI Methods": "Predictive modeling, trial analytics, automation",
        "Therapeutic Areas": "Broad",
        "Delivery Relevance (0-5)": 3,
        "Implant Fit (0-5)": 2,
        "Clinical Stage Strength (0-5)": 5,
        "Partnership Openness (0-5)": 2,
        "Trend Tags": "clinical analytics, predictive modeling, automation, real-world evidence",
        "Notes": "Large scale partner; slower to move but high capability."
    },
    {
        "Company": "Novartis",
        "Type": "Big pharma",
        "Primary Focus": "Drug development",
        "AI Methods": "Predictive modeling, digital platforms",
        "Therapeutic Areas": "Broad",
        "Delivery Relevance (0-5)": 3,
        "Implant Fit (0-5)": 2,
        "Clinical Stage Strength (0-5)": 5,
        "Partnership Openness (0-5)": 2,
        "Trend Tags": "predictive modeling, digital health, clinical analytics, automation",
        "Notes": "Strong R&D; could be strategic but may be selective."
    },
    {
        "Company": "MIT (selected labs)",
        "Type": "Research institution",
        "Primary Focus": "Drug delivery",
        "AI Methods": "Modeling, optimization, experimental automation",
        "Therapeutic Areas": "Broad",
        "Delivery Relevance (0-5)": 4,
        "Implant Fit (0-5)": 3,
        "Clinical Stage Strength (0-5)": 1,
        "Partnership Openness (0-5)": 4,
        "Trend Tags": "drug delivery, long-acting, modeling, optimization, lab automation",
        "Notes": "Academic collaboration potential; early-stage innovation."
    },
    {
        "Company": "ETH Zurich (selected groups)",
        "Type": "Research institution",
        "Primary Focus": "Materials & drug delivery",
        "AI Methods": "Modeling, materials informatics, automation",
        "Therapeutic Areas": "Broad",
        "Delivery Relevance (0-5)": 4,
        "Implant Fit (0-5)": 4,
        "Clinical Stage Strength (0-5)": 1,
        "Partnership Openness (0-5)": 4,
        "Trend Tags": "materials informatics, implants, drug delivery, automation, predictive modeling",
        "Notes": "Materials + delivery alignment; good for implants/materials questions."
    },
    {
        "Company": "NVIDIA (BioNeMo ecosystem)",
        "Type": "Big tech",
        "Primary Focus": "AI platform",
        "AI Methods": "Foundation models, acceleration, tooling",
        "Therapeutic Areas": "Broad",
        "Delivery Relevance (0-5)": 2,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 1,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "AI platform, foundation models, compute acceleration, generative AI",
        "Notes": "Enabler partner, not a delivery company."
    },
    {
        "Company": "EQRx",
        "Type": "Public company",
        "Primary Focus": "Drug development",
        "AI Methods": "Predictive modeling, cost optimization",
        "Therapeutic Areas": "Oncology, chronic disease",
        "Delivery Relevance (0-5)": 2,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 3,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "drug development, analytics, cost optimization, commercialization",
        "Notes": "Focus on affordable drug development; limited delivery innovation."
    },
    {
        "Company": "Capsida Biotherapeutics",
        "Type": "Startup",
        "Primary Focus": "Drug delivery",
        "AI Methods": "ML-guided capsid engineering",
        "Therapeutic Areas": "Gene therapy, CNS",
        "Delivery Relevance (0-5)": 4,
        "Implant Fit (0-5)": 2,
        "Clinical Stage Strength (0-5)": 2,
        "Partnership Openness (0-5)": 4,
        "Trend Tags": "gene delivery, AAV, capsid engineering, ML, targeted delivery",
        "Notes": "Advanced delivery engineering; more viral than implant-based."
    },
    {
        "Company": "Generate Biomedicines",
        "Type": "Startup",
        "Primary Focus": "Drug discovery",
        "AI Methods": "Generative protein design",
        "Therapeutic Areas": "Protein therapeutics",
        "Delivery Relevance (0-5)": 2,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 2,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "generative AI, protein design, biologics, predictive modeling",
        "Notes": "Strong generative AI; indirect relevance to delivery."
    },
    {
        "Company": "Cour Pharmaceuticals",
        "Type": "Startup",
        "Primary Focus": "Drug delivery",
        "AI Methods": "Modeling of immune tolerance delivery systems",
        "Therapeutic Areas": "Autoimmune disease",
        "Delivery Relevance (0-5)": 4,
        "Implant Fit (0-5)": 3,
        "Clinical Stage Strength (0-5)": 3,
        "Partnership Openness (0-5)": 4,
        "Trend Tags": "drug delivery, immunology, targeted delivery, predictive modeling, long-acting",
        "Notes": "Specialized delivery systems with potential for long-acting platforms."
    },
    {
        "Company": "Verge Genomics",
        "Type": "Startup",
        "Primary Focus": "Drug discovery",
        "AI Methods": "Network-based ML, target identification",
        "Therapeutic Areas": "Neurodegenerative disease",
        "Delivery Relevance (0-5)": 1,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 2,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "target identification, network biology, ML, neuroscience",
        "Notes": "Discovery-focused; delivery relevance is low."
    },
    {
        "Company": "Arctoris",
        "Type": "Private company",
        "Primary Focus": "Drug discovery",
        "AI Methods": "Robotics, ML-driven experimentation",
        "Therapeutic Areas": "Broad",
        "Delivery Relevance (0-5)": 2,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 2,
        "Partnership Openness (0-5)": 4,
        "Trend Tags": "lab automation, robotics, high-throughput screening, ML, closed-loop experimentation",
        "Notes": "Automation platform; could support formulation workflows."
    },
    {
        "Company": "Owkin",
        "Type": "Private company",
        "Primary Focus": "Drug discovery",
        "AI Methods": "Federated learning, multimodal ML",
        "Therapeutic Areas": "Oncology",
        "Delivery Relevance (0-5)": 1,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 3,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "federated learning, multimodal ML, clinical data, oncology",
        "Notes": "Clinical data AI; limited delivery relevance."
    },
    {
        "Company": "Polaris Quantum Biotech",
        "Type": "Startup",
        "Primary Focus": "Drug discovery",
        "AI Methods": "Quantum-inspired ML",
        "Therapeutic Areas": "Oncology",
        "Delivery Relevance (0-5)": 1,
        "Implant Fit (0-5)": 1,
        "Clinical Stage Strength (0-5)": 1,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "quantum computing, quantum-inspired ML, molecular modeling, early-stage",
        "Notes": "Early-stage discovery focus; speculative delivery impact."
    },
    {
        "Company": "Nanobiotix",
        "Type": "Public company",
        "Primary Focus": "Drug delivery",
        "AI Methods": "Modeling of nanoparticle interactions",
        "Therapeutic Areas": "Oncology",
        "Delivery Relevance (0-5)": 4,
        "Implant Fit (0-5)": 3,
        "Clinical Stage Strength (0-5)": 4,
        "Partnership Openness (0-5)": 3,
        "Trend Tags": "nanoparticles, targeted delivery, oncology, predictive modeling, intratumoral delivery",
        "Notes": "Nanoparticle-based delivery; closer alignment with physical delivery systems."
    },
    {
        "Company": "Aspect Biosystems",
        "Type": "Startup",
        "Primary Focus": "Drug delivery",
        "AI Methods": "AI-driven bioprinting and materials optimization",
        "Therapeutic Areas": "Regenerative medicine",
        "Delivery Relevance (0-5)": 4,
        "Implant Fit (0-5)": 4,
        "Clinical Stage Strength (0-5)": 2,
        "Partnership Openness (0-5)": 4,
        "Trend Tags": "bioprinting, biomaterials, implants, regenerative medicine, automation",
        "Notes": "Strong materials + structure focus; relevant for implant-based strategies."
    },
]
if "companies" not in st.session_state:
    st.session_state.companies = pd.DataFrame(STARTER_COMPANIES)

df = st.session_state.companies.copy()


# -----------------------------
# Trend Tags support (Upgrade)
# -----------------------------
# Ensure Trend Tags exists even if older entries don't include it yet
if "Trend Tags" not in df.columns:
    df["Trend Tags"] = ""
df["Trend Tags"] = df["Trend Tags"].fillna("")

# -----------------------------
# 2) Scoring model (editable)
# -----------------------------
st.sidebar.header("Scoring model (Best Fit for Hera)")

w_delivery = st.sidebar.slider("Weight: Delivery relevance", 0.0, 3.0, 1.4, 0.1)
w_implant = st.sidebar.slider("Weight: Implant fit", 0.0, 3.0, 1.6, 0.1)
w_clinical = st.sidebar.slider("Weight: Clinical-stage strength", 0.0, 3.0, 0.9, 0.1)
w_open = st.sidebar.slider("Weight: Partnership openness", 0.0, 3.0, 1.1, 0.1)

def compute_fit_score(row):
    score = (
        w_delivery * row["Delivery Relevance (0-5)"] +
        w_implant * row["Implant Fit (0-5)"] +
        w_clinical * row["Clinical Stage Strength (0-5)"] +
        w_open * row["Partnership Openness (0-5)"]
    )
    max_score = (w_delivery + w_implant + w_clinical + w_open) * 5
    pct = 0 if max_score == 0 else (score / max_score) * 100
    return score, pct

df[["Fit Score (raw)", "Fit Score (%)"]] = df.apply(lambda r: pd.Series(compute_fit_score(r)), axis=1)

# -----------------------------
# 3) Filters
# -----------------------------
st.sidebar.header("Filters")

type_filter = st.sidebar.multiselect("Type", sorted(df["Type"].unique().tolist()), default=sorted(df["Type"].unique().tolist()))
focus_filter = st.sidebar.multiselect("Primary Focus", sorted(df["Primary Focus"].unique().tolist()), default=sorted(df["Primary Focus"].unique().tolist()))
min_fit = st.sidebar.slider("Minimum Fit Score (%)", 0, 100, 0, 1)
# -----------------------------
# Trend Tag filter (Upgrade)
# -----------------------------
def parse_tags(tag_str: str):
    return [t.strip().lower() for t in (tag_str or "").split(",") if t.strip()]

all_tags = sorted({t for s in df["Trend Tags"].tolist() for t in parse_tags(s)})

tag_filter = st.sidebar.multiselect(
    "Trend tags",
    options=all_tags,
    default=[]
)

def passes_tag_filter(row) -> bool:
    if not tag_filter:
        return True
    row_tags = set(parse_tags(row["Trend Tags"]))
    return any(t in row_tags for t in tag_filter)

filtered = df[
    df["Type"].isin(type_filter) &
    df["Primary Focus"].isin(focus_filter) &
    (df["Fit Score (%)"] >= min_fit) &
    (df.apply(passes_tag_filter, axis=1))
].sort_values("Fit Score (%)", ascending=False)

# -----------------------------
# 4) Main view
# -----------------------------
left, right = st.columns([2, 1])

with left:
    st.subheader("Ranked partner list")
    show_cols = [
        "Company", "Type", "Primary Focus", "Trend Tags",
        "Delivery Relevance (0-5)", "Implant Fit (0-5)",
        "Clinical Stage Strength (0-5)", "Partnership Openness (0-5)",
        "Fit Score (%)"
    ]
    st.dataframe(filtered[show_cols], use_container_width=True, hide_index=True)

    st.caption("Tip: adjust weights in the sidebar to match Hera’s strategy. Higher Implant Fit + Delivery Relevance usually matters most.")

with right:
    st.subheader("Quick insights")
    st.metric("Companies in view", len(filtered))
    if len(filtered) > 0:
        top = filtered.iloc[0]
        st.success(f"Top pick right now: {top['Company']} ({top['Fit Score (%)']:.1f}%)")
        st.write("Why it ranks high (based on your weights):")
        st.write(f"- Delivery relevance: {top['Delivery Relevance (0-5)']}/5")
        st.write(f"- Implant fit: {top['Implant Fit (0-5)']}/5")
        st.write(f"- Partnership openness: {top['Partnership Openness (0-5)']}/5")
        st.write(f"- Notes: {top['Notes']}")

st.divider()

# -----------------------------
# 5) Company detail viewer
# -----------------------------
st.subheader("Company detail")
company_names = filtered["Company"].tolist() if len(filtered) > 0 else df["Company"].tolist()
selected = st.selectbox("Select a company", company_names)

row = df[df["Company"] == selected].iloc[0]
# -----------------------------
# Auto Recommendation Summary (Upgrade)
# -----------------------------
def recommendation_summary(row, w_delivery, w_implant, w_clinical, w_open) -> str:
    weights = {
        "delivery": w_delivery,
        "implant": w_implant,
        "clinical": w_clinical,
        "openness": w_open
    }
    top_priority = max(weights, key=weights.get)

    delivery = int(row["Delivery Relevance (0-5)"])
    implant = int(row["Implant Fit (0-5)"])
    clinical = int(row["Clinical Stage Strength (0-5)"])
    open_ = int(row["Partnership Openness (0-5)"])
    fit = float(row["Fit Score (%)"])

    strengths = []
    risks = []

    if delivery >= 4:
        strengths.append("strong delivery relevance")
    elif delivery <= 2:
        risks.append("limited direct delivery alignment")

    if implant >= 4:
        strengths.append("high compatibility with implant-based strategies")
    elif implant <= 2:
        risks.append("weak fit with implant-based delivery")

    if clinical >= 4:
        strengths.append("strong clinical maturity")
    elif clinical <= 2:
        risks.append("early maturity, may require longer timelines")

    if open_ >= 4:
        strengths.append("high collaboration potential")
    elif open_ <= 2:
        risks.append("may be harder to partner with quickly")

    strategy_map = {
        "delivery": "delivery relevance",
        "implant": "implant fit",
        "clinical": "clinical maturity",
        "openness": "partnership openness"
    }
    strategy_line = f"Given your current weights, the model prioritizes {strategy_map[top_priority]} most."

    if fit >= 75:
        verdict = "Recommended partner candidate."
    elif fit >= 55:
        verdict = "Promising, but depends on the partnership goal."
    else:
        verdict = "Lower priority under the current strategy."

    strengths_txt = "Strengths: " + (", ".join(strengths) if strengths else "no strong signals from the current scores.")
    risks_txt = "Risks: " + (", ".join(risks) if risks else "no major red flags indicated by the current scores.")

    tag_str = str(row.get("Trend Tags", "")).strip()
    tag_line = f"Trend tags: {tag_str}" if tag_str else "Trend tags: none added yet."

    return (
        f"{verdict} Fit Score: {fit:.1f}%. "
        f"{strategy_line} "
        f"{strengths_txt} "
        f"{risks_txt} "
        f"{tag_line}"
    )
c1, c2 = st.columns([2, 2])
with c1:
    st.write("**Summary**")
    st.write(f"- Type: {row['Type']}")
    st.write(f"- Primary focus: {row['Primary Focus']}")
    st.write(f"- AI methods: {row['AI Methods']}")
    st.write(f"- Therapeutic areas: {row['Therapeutic Areas']}")
with c2:
    st.write("**Fit scores**")
    st.write(f"- Fit Score (%): {row['Fit Score (%)']:.1f}")
    st.write(f"- Delivery relevance: {row['Delivery Relevance (0-5)']}/5")
    st.write(f"- Implant fit: {row['Implant Fit (0-5)']}/5")
    st.write(f"- Clinical stage strength: {row['Clinical Stage Strength (0-5)']}/5")
    st.write(f"- Partnership openness: {row['Partnership Openness (0-5)']}/5")

st.write("**Notes**")
st.write(row["Notes"])
st.subheader("Auto recommendation (copy into report)")
st.write(recommendation_summary(row, w_delivery, w_implant, w_clinical, w_open))
st.divider()
# -----------------------------
# 6) Add a company (your research -> tool)
# -----------------------------
st.subheader("Add a company (as you research)")

with st.form("add_company_form", clear_on_submit=True):
    new_company = st.text_input("Company name")
    new_type = st.selectbox(
        "Type",
        ["Startup", "Private company", "Public company", "Big pharma", "Big tech", "Research institution", "Other"]
    )
    new_focus = st.selectbox(
        "Primary focus",
        ["Drug discovery", "Drug delivery", "Drug development", "Computational modeling", "Manufacturing automation", "AI platform", "Other"]
    )
    new_methods = st.text_input("AI methods (short)")
    new_areas = st.text_input("Therapeutic areas (short)")
    new_tags = st.text_input("Trend tags (comma-separated)", help="Example: long-acting, implants, automation")

    colA, colB, colC, colD = st.columns(4)
    with colA:
        new_delivery = st.slider("Delivery relevance (0-5)", 0, 5, 2)
    with colB:
        new_implant = st.slider("Implant fit (0-5)", 0, 5, 2)
    with colC:
        new_clinical = st.slider("Clinical-stage strength (0-5)", 0, 5, 2)
    with colD:
        new_open = st.slider("Partnership openness (0-5)", 0, 5, 3)

    new_notes = st.text_area("Notes (1–2 sentences)")
    submitted = st.form_submit_button("Add company")

if submitted:
    if new_company.strip() == "":
        st.error("Company name cannot be blank.")
    else:
        new_row = {
            "Company": new_company.strip(),
            "Type": new_type,
            "Primary Focus": new_focus,
            "AI Methods": new_methods.strip(),
            "Therapeutic Areas": new_areas.strip(),
            "Delivery Relevance (0-5)": int(new_delivery),
            "Implant Fit (0-5)": int(new_implant),
            "Clinical Stage Strength (0-5)": int(new_clinical),
            "Partnership Openness (0-5)": int(new_open),
            "Trend Tags": new_tags.strip(),
            "Notes": new_notes.strip()
        }
        st.session_state.companies = pd.concat(
            [st.session_state.companies, pd.DataFrame([new_row])],
            ignore_index=True
        )
        st.success(f"Added: {new_company.strip()}")
# -----------------------------
# 7) Export
# -----------------------------
st.subheader("Export")
export_df = st.session_state.companies.copy()


export_df[["Fit Score (raw)", "Fit Score (%)"]] = export_df.apply(lambda r: pd.Series(compute_fit_score(r)), axis=1)

csv = export_df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", data=csv, file_name="ai_partner_landscape.csv", mime="text/csv")

st.caption("Export this CSV and use it to build your structured internship report tables.")



