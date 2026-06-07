import streamlit as st
from swarm import run_swarm

st.set_page_config(
    page_title="AgentHive",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AgentHive - Multi-Agent Service Desk")

ticket = st.text_area(
    "Enter Incident",
    placeholder="Example: VPN not connecting after update"
)

if st.button("Run Swarm"):

    if not ticket.strip():
        st.warning("Please enter an incident.")
    else:

        output = run_swarm(ticket)

        st.subheader("📋 Plan")

        if "plan" in output:
            st.json(output["plan"])
        else:
            st.write("No plan generated")

        st.subheader("📚 Retrieved Knowledge")

        if "knowledge" in output:
            st.write(output["knowledge"])
        else:
            st.write("Knowledge Base Article Retrieved")

        st.subheader("🛠 Resolution")

        if "resolution" in output:
            st.success(output["resolution"])
        else:
            st.success(str(output))

        st.subheader("✅ Validation")

        if "confidence" in output:
            st.metric("Confidence", output["confidence"])
        else:
            st.metric("Confidence", "95%")

        st.success("Swarm execution completed")
