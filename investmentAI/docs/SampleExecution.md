# 🚀 Investment AI Assistant - Sample Execution

This document demonstrates the end-to-end execution flow of the Investment AI Assistant built using **Google ADK**, **Gemini 2.5 Flash**, and **RAG with ChromaDB**.

---

## User Query

```text
What is SIP?
```

---

## Step 1 - Intent Detection

```text
Intent      : INVESTMENT
Confidence  : 0.98
Reason      : User is asking for an explanation of an investment term (SIP).
```

---

## Step 2 - Route Selection

```text
✓ Routed to Investment Workflow
```

---

## Step 3 - Retrieval (RAG)

```text
Tool Invoked:
retrieve_documents()

Retrieved Documents : 3

✓ Document 1
Systematic Investment Plan (SIP)

✓ Document 2
What is SIP?

✓ Document 3
Features of SIP
```

---

## Step 4 - Recommendation Generation

```text
A Systematic Investment Plan (SIP) is a feature provided by
mutual funds that enables investors to invest in a disciplined
manner.

It allows investors to invest a fixed amount at regular
intervals such as weekly, monthly, or quarterly.

Benefits include:

• Disciplined investing
• Rupee Cost Averaging
• Professional Fund Management
• Potential Long-term Wealth Creation
```

---

## Step 5 - Compliance Review

```text
Status : APPROVED

Validation Checks

✓ Accuracy
✓ Hallucination
✓ Guaranteed Returns
✓ Risk Disclosure
✓ Professional Language
```

---

## Final Response

```text
A Systematic Investment Plan (SIP) is a feature provided by
mutual funds that enables investors to invest in a disciplined
manner.

It allows investors to invest a fixed amount at regular
intervals such as weekly, monthly, or quarterly.

Benefits include:

• Disciplined investing
• Rupee Cost Averaging
• Professional Fund Management
• Potential Long-term Wealth Creation

------------------------------------------------------------

Disclaimer:

This information is for educational purposes only and should
not be considered personalized financial advice.

Please consult a qualified financial advisor before making
investment decisions.
```

---

## Execution Summary

| Stage | Status |
|--------|--------|
| Intent Detection | ✅ Success |
| Agent Routing | ✅ Success |
| Document Retrieval | ✅ Success |
| Recommendation Generation | ✅ Success |
| Compliance Validation | ✅ Approved |
| Final Response | ✅ Returned |

---

## Architecture Used

- Google ADK Multi-Agent Framework
- Intent Routing Agent
- Retrieval Agent (RAG)
- Chroma Vector Database
- Gemini 2.5 Flash
- Compliance Validation Agent
- Automatic Disclaimer Injection





## Console Output

(venv) amitpal@Amits-MacBook-Pro GoogleADK % python -m investmentAI.runner
/Users/amitpal/Desktop/GitRepos/GoogleADK/investmentAI/rag/retriever.py:9: LangChainDeprecationWarning: The class `Chroma` was deprecated in LangChain 0.2.9 and will be removed in 1.0. An updated version of the class exists in the `langchain-chroma package and should be used instead. To use it run `pip install -U `langchain-chroma` and import as `from `langchain_chroma import Chroma``.
  vector_store = Chroma(

================================================================================
 User Request
================================================================================

--------------------------------------------------------------------------------
Query
--------------------------------------------------------------------------------
What is SIP?

================================================================================
 Intent Agent
================================================================================

--------------------------------------------------------------------------------
Agent Output
--------------------------------------------------------------------------------
{"intent":"INVESTMENT","confidence":0.99,"reason":"Query about an investment product (SIP)."}

================================================================================
 Intent Detection
================================================================================

--------------------------------------------------------------------------------
Detected Intent
--------------------------------------------------------------------------------
 Intent      : INVESTMENT Confidence  : 0.99 Reason      : Query about an investment product (SIP).

================================================================================
 Investment Workflow - Attempt 1
================================================================================
Event from an unknown agent: intent_agent, event id: 44511c53-45c7-476a-ab4a-8f46af6c6ae9
/Users/amitpal/Desktop/GitRepos/GoogleADK/venv/lib/python3.11/site-packages/google/adk/tools/function_tool.py:95: UserWarning: [EXPERIMENTAL] feature FeatureName.JSON_SCHEMA_FOR_FUNC_DECL is enabled.
  build_function_declaration(

================================================================================
 Investment Agent
================================================================================

--------------------------------------------------------------------------------
Agent Output
--------------------------------------------------------------------------------
A Systematic Investment Plan (SIP) is a facility offered by mutual funds that allows investors to
invest in a disciplined manner. Through a SIP, an investor can invest a fixed amount of money at
pre-defined intervals, such as weekly, monthly, quarterly, semi-annually, or annually. The minimum
investment can be as low as Rs. 500.  SIPs operate on the principle of regularity and periodicity,
enabling investors to contribute small sums over an extended period. This approach promotes
disciplined investment and helps investors benefit in the long term through average costing and the
power of compounding, without needing to constantly worry about market dynamics. Additionally, SIPs
provide access to professionally managed mutual funds, where experienced fund managers make
investment decisions based on in-depth research and market analysis.

--------------------------------------------------------------------------------
Generated Recommendation
--------------------------------------------------------------------------------
A Systematic Investment Plan (SIP) is a facility offered by mutual funds that allows investors to
invest in a disciplined manner. Through a SIP, an investor can invest a fixed amount of money at
pre-defined intervals, such as weekly, monthly, quarterly, semi-annually, or annually. The minimum
investment can be as low as Rs. 500.  SIPs operate on the principle of regularity and periodicity,
enabling investors to contribute small sums over an extended period. This approach promotes
disciplined investment and helps investors benefit in the long term through average costing and the
power of compounding, without needing to constantly worry about market dynamics. Additionally, SIPs
provide access to professionally managed mutual funds, where experienced fund managers make
investment decisions based on in-depth research and market analysis.
Event from an unknown agent: retrieval_agent, event id: cc62dec0-4998-4150-bf72-8d08b5d91ecc
Event from an unknown agent: retrieval_agent, event id: cf7070c8-d694-4a16-9fa8-edf67d5121af
Event from an unknown agent: retrieval_agent, event id: 56c969c6-7d33-4186-98cf-d0cdd7242388
Event from an unknown agent: intent_agent, event id: 44511c53-45c7-476a-ab4a-8f46af6c6ae9

================================================================================
 Compliance Agent
================================================================================

--------------------------------------------------------------------------------
Agent Output
--------------------------------------------------------------------------------
REJECTED  Reason: - Risk Disclosure

================================================================================
 Compliance Review
================================================================================
❌ Compliance Status : REJECTED

--------------------------------------------------------------------------------
Compliance Output
--------------------------------------------------------------------------------
REJECTED  Reason: - Risk Disclosure
❌ Retrying Investment Agent...

================================================================================
 Investment Workflow - Attempt 2
================================================================================
Event from an unknown agent: compliance_agent, event id: 4270ec81-4dc9-449e-b40c-824e43b67ea0
Event from an unknown agent: intent_agent, event id: 44511c53-45c7-476a-ab4a-8f46af6c6ae9

================================================================================
 Investment Agent
================================================================================

--------------------------------------------------------------------------------
Agent Output
--------------------------------------------------------------------------------
A Systematic Investment Plan (SIP) is a facility offered by mutual funds that allows investors to
invest in a disciplined manner. Through a SIP, an investor can invest a fixed amount of money at
pre-defined intervals, such as weekly, monthly, quarterly, semi-annually, or annually. The minimum
investment can be as low as Rs. 500.  SIPs operate on the principle of regularity and periodicity,
enabling investors to contribute small sums over an extended period. This approach promotes
disciplined investment and helps investors benefit in the long term through average costing and the
power of compounding, without needing to constantly worry about market dynamics. Additionally, SIPs
provide access to professionally managed mutual funds, where experienced fund managers make
investment decisions based on in-depth research and market analysis.  Mutual fund investments are
subject to market risks. Please read the offer document carefully before investing.

--------------------------------------------------------------------------------
Generated Recommendation
--------------------------------------------------------------------------------
A Systematic Investment Plan (SIP) is a facility offered by mutual funds that allows investors to
invest in a disciplined manner. Through a SIP, an investor can invest a fixed amount of money at
pre-defined intervals, such as weekly, monthly, quarterly, semi-annually, or annually. The minimum
investment can be as low as Rs. 500.  SIPs operate on the principle of regularity and periodicity,
enabling investors to contribute small sums over an extended period. This approach promotes
disciplined investment and helps investors benefit in the long term through average costing and the
power of compounding, without needing to constantly worry about market dynamics. Additionally, SIPs
provide access to professionally managed mutual funds, where experienced fund managers make
investment decisions based on in-depth research and market analysis.  Mutual fund investments are
subject to market risks. Please read the offer document carefully before investing.
Event from an unknown agent: retrieval_agent, event id: 0c5d5f91-c750-4033-a83b-4841f1df0d6b

================================================================================
 Compliance Agent
================================================================================

--------------------------------------------------------------------------------
Agent Output
--------------------------------------------------------------------------------
APPROVED

================================================================================
 Compliance Review
================================================================================
✅ Compliance Status : APPROVED

--------------------------------------------------------------------------------
Compliance Output
--------------------------------------------------------------------------------
APPROVED

================================================================================
 Final Response
================================================================================

--------------------------------------------------------------------------------
Response
--------------------------------------------------------------------------------
A Systematic Investment Plan (SIP) is a facility offered by mutual funds that allows investors to
invest in a disciplined manner. Through a SIP, an investor can invest a fixed amount of money at
pre-defined intervals, such as weekly, monthly, quarterly, semi-annually, or annually. The minimum
investment can be as low as Rs. 500.  SIPs operate on the principle of regularity and periodicity,
enabling investors to contribute small sums over an extended period. This approach promotes
disciplined investment and helps investors benefit in the long term through average costing and the
power of compounding, without needing to constantly worry about market dynamics. Additionally, SIPs
provide access to professionally managed mutual funds, where experienced fund managers make
investment decisions based on in-depth research and market analysis.  Mutual fund investments are
subject to market risks. Please read the offer document carefully before investing.
------------------------------------------------------------------  Disclaimer: This information is
for educational purposes only and should not be considered personalized financial advice. Please
consult a qualified financial advisor before making investment decisions.
(venv) amitpal@Amits-MacBook-Pro GoogleADK % 


