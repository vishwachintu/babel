import streamlit as st
import pandas as pd

# Define the data for Problem Statements
problem_statements_data = [
    {
        "Problem Statement": "Limited availability of real-world data hinders the quality of solution.",
        "Stakeholders": "Testing",
        "Outcomes": "Improve code quality and performance.",
    },
    {
        "Problem Statement": "Manual testing procedures hinder pace and quality of delivery.",
        "Stakeholders": "Data Analysts",
        "Outcomes": "Expedite solution delivery cycle.",
    },
    {
        "Problem Statement": "AI algorithms trained on biased datasets may perpetuate existing biases, resulting in unfair vendor selection outcomes.",
        "Stakeholders": "Privacy & Security",
        "Outcomes": "Improve collaboration between teams and reduce friction.",
    },
    {
        "Problem Statement": "Difficulty in scaling AI-based vendor selection processes to handle a large volume of vendors or changing business requirements efficiently.",
        "Stakeholders": "CIO",
        "Outcomes": "",
    },
]

# Define the data for Scope of Gen AI
scope_data = [
    {
        "Team/System/Capability": "Web Development",
        "Gen AI Use Cases": ["Code Generation"],
    },
    {
        "Team/System/Capability": "App Development",
        "Gen AI Use Cases": ["Code Translation", "Code Analysis"],
    },
    {
        "Team/System/Capability": "Testing",
        "Gen AI Use Cases": ["Defect Forecasting", "Automated Testing"],
    },
    {
        "Team/System/Capability": "Business Analysts",
        "Gen AI Use Cases": ["Requirements Generation", "Test Automation"],
    },
]

vendor_selection_criteria_data = {
    "Evaluation Criteria": [
        "Features & Functionalities",
        "Customization & Flexibility",
        "Support & Maintenance",
        "Scalability",
        "Ease of Integration & Deployment",
        "Security",
        "Affordability",
        "Vendor Viability & Vision",
    ],
    "Leading Questions": [
        "Does the vendor align with your top-priority use cases and functional and nonfunctional requirements? Is the solution's interface intuitive, accessible, and easy to use for the target end users?",
        "Does the vendor provide options to fine-tune or adapt the generative AI model to align with your creative vision or domain-specific constraints? Are popular programming languages, frameworks, and tactics used in the modification of Gen AI models, algorithms, or training methods?",
        "Is there a service-level agreement (SLA) that outlines the vendor's commitments regarding response times and issue resolution? Are there designated support channels, such as email, phone, or a dedicated support portal?",
        "Can additional resources be provisioned to ensure optimal processing speeds during high-volume events and handle increasing data volumes and user demands? Are your disaster recovery and business continuity requirements satisfied by the solution?",
        "Is the solution interoperable with existing applications, data infrastructure, and technologies in your stack? Does the solution meet your deployment and data residency preferences?",
        "Does this vendor comply with your organization’s security policies? Are training and operational data managed and governed separately to abide privacy and confidentiality requirements?",
        "Does the vendor provide transparent pricing information and options for different budget requirements? Are free or demo versions available for teams to test and experiment with the solution's features and capabilities?",
        "Are they an established player with a proven track record or a new and untested entrant to the market? Does the vendor have a cogent and realistic product roadmap?",
    ],
    "Weight": [20, 15, 15, 10, 10, 10, 10, 10],
    "Evaluation Score Considerations": [
        "Alignment to functional and nonfunctional requirements, satisfaction of use cases. Ease of use and intuitiveness of the UI and administration console, accuracy of unstructured prompts (e.g. voice). Output quality, alignment to organization's document and artifact standards, output copyright concerns. Number of standards satisfied in the solution, alignment to your ethics policies and organizational principles. Scope and practicality of vendor provided templates, shells, and prebuilt and pretrained models, quality of data to train prebuilt models (e.g. bias).",
        "Accessibility to Gen AI model, ease of customization, ability to align models to meet technical, ethical, and other quality standards. Technology foundations and frameworks of the Gen AI model (e.g. .NET). Availability of source code management and versioning capabilities. Scope of data types and structures compatible with the solution. Frequency of retraining of the Gen AI model using the past solution outcomes, ease to prepare training data for retraining.",
        "Alignment of SLAs to the team's support needs. Availability of various support channels. Quality of training and onboarding resources, including videos, tutorials, and personal support. Health of the community, number of members, degree of involvement of members, availability of collaboration features in the solution. Scope of the solution's administration console, alignment of administration capabilities to your IT policies, ability to track the inventory of deployed Gen AI bots.",
        "Capability to scale infrastructure when additional processing power is needed. Number of activities the solution can support at one given time, number of users who can use and modify the solution. Ease to transfer solution artifacts to and from this solution. Ease to schedule the execution of the solution, ease to integrated Gen AI activities with broader business process orchestration. Alignment to disaster recovery and business continuity requirements.",
        "System fit and compatibility. Deployment flexibility (e.g. on-premises, private, and public cloud), location of vendor-provided infrastructure. Alignment to enterprise architecture principles, designs, and standards. Extent of out-of-the-box plugins, availability of custom APIs into vendor solution; plugins/APIs as extensions into other solutions.",
        "Satisfaction of security, privacy and confidentiality policies. Data management and governance practices for training and operational data. Availability of access management and user monitoring. IP and data leakage protection protocols.",
        "Licensing costs, clarity of pricing structure, confidence in long-term cost estimates. Labor, training, and onboarding costs. Availability of fully featured free or demo versions of the solution. Operational costs.",
        "Age and version history of the solution, scope of deployed releases and fixes, history in the marketplace and industry. Alignment of the solution's vision and roadmap with your broader organization's strategy and roadmap. Participation in open-source communities, involvement in conferences. Size and diversity of the vendor's portfolio, investments in the innovation and modernization of their Gen AI solutions.",
    ],
    "Notes": ["", "", "", "", "", "", "", ""],
}

vendors = ["Vendor A", "Vendor B", "Vendor C"]

# Define the criteria, weights, and questions
criteria = {
    "Features & Functionalities": {
        "weight": 0.20,
        "questions": [
            "Does the vendor align with your top-priority use cases and functional and nonfunctional requirements?",
            "Is the solution's interface intuitive, accessible, and easy to use for the target end users?",
            "Can the solution generate valuable outputs in the desired formats or mediums (e.g., images, music, text)? Does the generated output conflict with copyrights?",
            "Does the vendor provide out-of-the-box compliance to industry and regulatory standards? Does the solution align with your ethics policies and principles?",
            "Are templates, shells, and pretrained models and bots readily available? What data was used to train the prebuilt models?",
        ],
    },
    "Customization & Flexibility": {
        "weight": 0.15,
        "questions": [
            "Does the vendor provide options to fine-tune or adapt the generative AI model to align with your creative vision or domain-specific constraints?",
            "Are popular programming languages, frameworks, and tactics used in the modification of Gen AI models, algorithms, or training methods?",
            "Are all changes and modifications to the Gen AI model catalogued and versioned?",
            "Is the Gen AI model compatible with a variety of data types and structures?",
            "Is the Gen AI model continuously retrained with fresh data?",
        ],
    },
    "Support & Maintenance": {
        "weight": 0.15,
        "questions": [
            "Is there a service-level agreement (SLA) that outlines the vendor's commitments regarding response times and issue resolution?",
            "Are there designated support channels, such as email, phone, or a dedicated support portal?",
            "Does the vendor provide training and onboarding?",
            "Can multiple users or teams collaborate within the solution? Does the vendor provide forums to enable discussion and sharing among peers?",
            "Does the solution provide a dashboard to monitor the modifications, uses, value, and performances of the Gen AI bots?",
        ],
    },
    "Scalability": {
        "weight": 0.10,
        "questions": [
            "Can additional resources be provisioned to ensure optimal processing speeds during high-volume events and handle increasing data volumes and user demands?",
            "Are there any licensing, load, or traffic constraints of the solution?",
            "How easy is it to transfer models, training data, and other solution artifacts to and from this solution?",
            "Can the solution's execution be timed, planned, and orchestrated according to the user's preferred schedule or workflow triggers?",
            "Are your disaster recovery and business continuity requirements satisfied by the solution?",
        ],
    },
    "Ease of Integration & Deployment": {
        "weight": 0.10,
        "questions": [
            "Is the solution interoperable with existing applications, data infrastructure, and technologies in your stack?",
            "Does the solution meet your deployment and data residency preferences?",
            "Does this vendor align with your direction from an enterprise architecture perspective?",
            "Does the vendor provide out-of-the-box plugins and customizable APIs to support integration with other solutions?",
        ],
    },
    "Security": {
        "weight": 0.10,
        "questions": [
            "Does this vendor comply with your organization's security policies?",
            "Are training and operational data managed and governed separately to abide privacy and confidentiality requirements?",
            "Does the solution provide role-based access and monitor user activities?",
            "Does the vendor provide sufficient protection of their Gen AI bots to prevent IP and data leakage?",
        ],
    },
    "Affordability": {
        "weight": 0.10,
        "questions": [
            "Does the vendor provide transparent pricing information and options for different budget requirements?",
            "Do you need to bring in or train specialized labor to implement and maintain the solution (e.g. FTE developers or BI analysts)?",
            "Are free or demo versions available for teams to test and experiment with the solution's features and capabilities?",
            "What is the cost to leverage vendor infrastructure to operate and support the solution?",
        ],
    },
    "Vendor Viability & Vision": {
        "weight": 0.10,
        "questions": [
            "Are they an established player with a proven track record or a new and untested entrant to the market? What is the financial health of the vendor?",
            "Does the vendor have a cogent and realistic product roadmap? Are they making sensible investments that align with your organization’s internal direction?",
            "Does the vendor engage and collaborate with peers in the industry and marketplace?",
            "What is the scope of Gen AI solutions in the vendor's portfolio? How committed are they to the particular solution category?",
        ],
    },
}


# Create a sidebar
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio(
    "Select a Page", ["Gen AI Vendor Canvas", "Vendor Selection Criteria"]
)

# Define content for each page
if selected_page == "Gen AI Vendor Canvas":
    st.title("Gen AI Vendor Canvas")

    # Display the Problem Statements table
    st.header("Problem Statements")
    problem_statements_df = pd.DataFrame(problem_statements_data)
    problem_statements_df = problem_statements_df.dropna()  # Remove empty rows
    problem_statements_df = problem_statements_df.reset_index(
        drop=True
    )  # Reset index starting from 1
    st.table(problem_statements_df[["Problem Statement"]])

    # Display the Stakeholders table
    st.header("Stakeholders")
    st.table(problem_statements_df[["Stakeholders"]])

    # Display the Outcomes table
    st.header("Outcomes")
    st.table(problem_statements_df[["Outcomes"]])

    # Display the Scope of Gen AI table
    st.header("Scope of Gen AI")
    scope_df = pd.DataFrame(scope_data)
    st.table(scope_df)

elif selected_page == "Vendor Selection Criteria":
    st.title("Vendor Selection Criteria")

    st.write(
        "This app allows you to evaluate vendors based on various criteria. Please select a vendor and enter scores for each question (1 to 5)."
    )

    # Select vendor
    selected_vendor = st.selectbox("Select Vendor", vendors)

    # Initialize an empty DataFrame to store scores
    scores = []

    # Collect scores
    for criterion, data in criteria.items():
        weight = data["weight"]
        st.header(f"{criterion} (Weight: {weight * 100}%)")

        for question in data["questions"]:
            score = st.slider(
                question, 1, 5, 3, key=f"{selected_vendor}-{criterion}-{question}"
            )
            scores.append(
                {
                    "Vendor": selected_vendor,
                    "Criteria": criterion,
                    "Weight": weight,
                    "Question": question,
                    "Score": score,
                }
            )

    # Convert to DataFrame
    scores_df = pd.DataFrame(scores)

    # Calculate weighted scores
    scores_df["Weighted Score"] = scores_df["Score"] * scores_df["Weight"]

    # Summarize results
    summary = (
        scores_df.groupby(["Vendor", "Criteria"])
        .agg(
            total_score=pd.NamedAgg(column="Weighted Score", aggfunc="sum"),
            max_score=pd.NamedAgg(column="Weight", aggfunc="sum"),
        )
        .reset_index()
    )

    summary["Total Weight"] = summary["max_score"]
    summary["Normalized Score"] = summary["total_score"] / summary["Total Weight"] * 100

    st.header("Evaluation Summary")
    st.dataframe(summary)

    # Display overall score for the selected vendor
    vendor_scores = summary[summary["Vendor"] == selected_vendor]
    overall_score = (
        vendor_scores["total_score"].sum() / vendor_scores["Total Weight"].sum() * 100
    )
    vendor_scores=(vendor_scores/500)*100
    st.write(f"**Overall Score for {selected_vendor}: {overall_score:.2f}%**")


# Footer


# Run the app
if __name__ == "__main__":
    pass  # No additional code is required here
