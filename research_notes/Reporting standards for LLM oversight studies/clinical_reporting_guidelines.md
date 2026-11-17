# Reporting guidelines and publication conventions for a clinical LLM evaluation study (as of November 2026)

## Q1. Which guidelines apply, and what does each cover?

### Takeaway
TRIPOD-LLM (Nature Medicine, Jan 2025) is the best fit: it names "LLM evaluation" as a design and "classification" as a task, and it has explicit items on prompts, settings, annotators, agreement and open science. MI-CLEAR-LLM (2025 update) is the best short companion for model identification, prompts, stochasticity and test-data contamination. CHART is built for chatbot health advice, so it fits only loosely (the checkers classify answers; they do not advise). No LLM-as-judge-specific medical guideline was found.

### Cited Findings
- TRIPOD-LLM: Gallifant et al., Nature Medicine 31(1):60-69, published 8 Jan 2025, DOI 10.1038/s41591-024-03425-5. 19 main items, 50 subitems; modular (items shown depend on design and task); living guideline; interactive checklist site tripod-llm.vercel.app. [PubMed 39779929](https://pubmed.ncbi.nlm.nih.gov/39779929/); [TRIPOD page](https://www.tripod-statement.org/tripod-llm/) (checklist PDF, E&E and worked example downloadable; no 2026 update notes on that page)
- TRIPOD-LLM workflow starts at 59 reporting items and filters down by design and task; 64 unique candidate items before consensus; registered with EQUATOR 2 May 2024. [Korean translation, Ewha Med J 2025, PMC12362290](https://pmc.ncbi.nlm.nih.gov/articles/PMC12362290/) (English parts and Table 2 read via Europe PMC)
- TRIPOD-LLM recommends its use for text processing, classification, information retrieval and summarisation, for single or multi-LLM comparison. [npj Digit Med comment, 7 Nov 2025](https://doi.org/10.1038/s41746-025-02113-z)
- MI-CLEAR-LLM: original Park, Suh, Lee, Kahn, Moy, Korean J Radiol 2024;25(10):865-868 (12 Sep 2024). 2025 update Park, Suh, Lee, Tejani, You, Kahn, Moy, Korean J Radiol 26(12):1123-1132, accepted 16 Oct 2025, epub 3 Nov 2025, DOI 10.3348/kjr.2025.1522. Eight item categories (not numbered items), each with several elements: model identification; access mode; input data type; adaptation strategy; prompt optimisation; prompt execution setup; stochasticity management; independence of test data. [Europe PMC full text PMC12683746](https://europepmc.org/article/MED/41199132)
- MI-CLEAR-LLM 2025 positions itself as narrower than TRIPOD-LLM/CHART and complementary to them. [same](https://europepmc.org/article/MED/41199132)
- CHART: 12 items, 39 subitems (abstract checklist: 9 items, 16 subitems), plus a methodological diagram. Statement published simultaneously (Aug-Sep 2025) in BMJ Medicine (10.1136/bmjmed-2025-001632), British Journal of Surgery 112(8) (10.1093/bjs/znaf142), BMC Medicine, Annals of Family Medicine (22 Sep 2025, 10.1370/afm.250386) and others; Explanation and Elaboration in BMJ 2025;390:e083305 (1 Aug 2025). Delphi of 531 stakeholders; 48-member expert panel. Scope: studies evaluating generative-AI chatbots summarising clinical evidence or giving health advice. [BMJ E&E, PMC12492839](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492839/); [LSE record](https://researchonline.lse.ac.uk/id/eprint/129124)
- STARD-AI: Sounderajah et al., Nature Medicine 31(10):3283-3289, published 15 Sep 2025, DOI 10.1038/s41591-025-03953-8. "18 new or modified items in addition to STARD 2015" (a mapping document describes a 40-item statement, 4 modified and 14 AI-specific; that is a third-party paraphrase). For diagnostic accuracy studies where an AI system is the index test; covers datasets, the AI index test, evaluation, bias and fairness. [Europe PMC record](https://europepmc.org/search?query=DOI:10.1038/s41591-025-03953-8); [EQUATOR listing](https://www.equator-network.org/reporting-guidelines/the-stard-ai-reporting-guideline-for-diagnostic-accuracy-studies-using-artificial-intelligence/)
- DECIDE-AI: Vasey et al., Nature Medicine, 18 May 2022, DOI 10.1038/s41591-022-01772-9. 17 AI-specific items (28 subitems) plus 10 generic items. Early-stage live clinical evaluation of AI decision support. [Europe PMC](https://europepmc.org/article/MED/35585198)
- CONSORT-AI (BMJ/Nature Med/Lancet Digit Health, 9 Sep 2020, e.g. 10.1136/bmj.m3164) and SPIRIT-AI: extensions for randomised trials/protocols of AI interventions; developed from 29 candidate items. [BMJ abstract via Europe PMC](https://europepmc.org/article/PMC/PMC7490784)
- CLAIM 2024 update: Radiology: Artificial Intelligence, 1 Jul 2024, DOI 10.1148/ryai.240300; for AI in medical imaging. [Europe PMC PMC11304031](https://europepmc.org/article/PMC/PMC11304031)
- MINIMAR: Hernandez-Boussard et al., JAMIA, 1 Dec 2020, DOI 10.1093/jamia/ocaa088; minimum information on data, model architecture, evaluation and generalisability for medical AI. [Europe PMC PMC7727333](https://europepmc.org/article/PMC/PMC7727333)
- TRIPOD+AI: BMJ 2024, 16 Apr 2024, 10.1136/bmj-2023-078378, for clinical prediction models (TRIPOD-LLM descends from it). [Europe PMC PMC11019967](https://europepmc.org/article/PMC/PMC11019967)
- Guideline map (npj Digit Med comment, 7 Nov 2025): LLM evaluation studies are covered by CHART, TRIPOD-LLM or GAMER (GAMER = use of generative AI in writing medical research, BMJ Evid Based Med 2025, 10.1136/bmjebm-2025-113825); CHART narrow scope, TRIPOD-LLM broad but item applicability depends on use case. In development: CANGARU, ELEVATE-GenAI (10 preliminary items, health economics), COREQ-LLM. [npj Digit Med](https://doi.org/10.1038/s41746-025-02113-z)
- Adherence study: basic LLM identification is reported fairly well, but stochasticity, prompts and test data are often underreported (Ko et al., Korean J Radiol 2025, as summarised by search). [Search summary of Korean J Radiol listing](https://ir.ymlib.yonsei.ac.kr/handle/22282913/210022)

### Inferences
- CONSORT-AI, SPIRIT-AI, DECIDE-AI, CLAIM, STARD-AI and MINIMAR are poor fits: no trial, no live clinical use, no imaging; STARD-AI frames the AI as a diagnostic index test on patients. Mention that they were considered and why they do not apply, in one line.
- Best pairing: TRIPOD-LLM as the primary checklist (submit it), with MI-CLEAR-LLM used as the detailed prompt/stochasticity/contamination crib; optionally cite CHART items 7a-7b, 8, 9a where useful. STARD 2015 logic (sensitivity/specificity vs a reference standard) is conceptually closest to the outcome definition, but STARD-AI is meant for patient-based diagnostic accuracy.

### Gaps
- Exact item counts not verified from the primary source for CONSORT-AI (my recollection is 14 new items; the sources opened gave only the 29 candidate items), CLAIM 2024, MINIMAR. Do not quote these counts without checking.
- The TRIPOD-LLM item table was read in a Korean translation (Ewha Med J, PMC12362290); the English Nature Medicine page and PMC page were blocked (captcha/redirect). Wording below is my back-translation; verify against the checklist PDF at tripod-statement.org.
- No 2025-2026 guideline specific to LLM-as-judge or LLM-checker studies in medicine was found (searched once, plus the npj Digit Med map); absence is not proven.
- A 2026 update of TRIPOD-LLM or CHART was not found; the TRIPOD page showed none.

## Q2. Checklist items that apply to this design

### Takeaway
Under TRIPOD-LLM the design is "LLM evaluation" (E), task "classification" (C), with no patient data (so items 16a-16d do not apply). The items that matter most are 5a-5e (test items), 6a/6c/6d/6e (model, settings, outputs, thresholds), 7d, 7e, 8a-8c (rater, labels, agreement), 9a-9b (prompts), 12 (compute), 13 (ethics), 14a-14f (funding, COI, protocol, registration, data, code), 17-19.

### Cited Findings
TRIPOD-LLM items (from the Table 2 of the translation; E = LLM evaluation, H = LLM evaluation in healthcare settings, C = classification; item applies if its design column includes E or says All and its task column includes C or says All) [PMC12362290](https://pmc.ncbi.nlm.nih.gov/articles/PMC12362290/):
- 1 Title: identify study as LLM evaluation, task, population, outcome. 2 Abstract: TRIPOD-LLM for Abstracts. 3a Background and rationale (all); 3b intended use and users (E,H). 4 Objectives.
- 5a Source of evaluation data and rationale (here: how the 48 synthetic questions were made); 5b dataset description and distribution; 5c earliest and latest dates of text; 5d preprocessing and quality checks; 5e missing/imbalanced data, exclusions.
- 6a LLM name, version and last training date; 6c text generation process, prompt engineering (incl. output consistency) and inference settings (seed, temperature, max tokens, penalties) (M,D,E); 6d initial and post-processed outputs (here: safe/unsafe label parsing); 6e classification details, probability and threshold identification (C).
- 7d When outcome needs subjective judgement: rater qualifications, instructions given, rater demographics, inter-rater agreement. 7e Comparator (LLM, human, other benchmark). 7b and 7c (E,H): suitability of the sub-task metric, how predictions were produced (formula, code, API), inference date for closed LLMs.
- 8a Annotation: how text was labelled, guidelines and examples; 8b number of annotators, proportion with multiple annotators, inter-annotator agreement; 8c annotator background and experience.
- 9a Prompt design, selection and selection process; 9b data used to develop prompts.
- 12 Compute or proxy (machines, time, cost, inference time) (M,D,E). 13 Ethical approval: name of IRB/ethics committee and consent or consent waiver; here a statement that none was needed and why.
- 14a Funding and funder role; 14b conflicts of interest of all authors; 14c protocol location or none (H); 14d registration registry and number or not registered (H); 14e data availability; 14f code availability for reproducibility.
- 15 Patient and public involvement (H). 16a-d patient/EHR data (EH): not applicable. 17 Report performance by the pre-specified metrics (7a) and/or human evaluation (7d). 18 LLM updating (if applicable). 19a interpretation incl. fairness; 19b limitations (bias, statistical uncertainty, generalisability); 19c-19f usability in context (E,H); 19g next steps.
- Note in TRIPOD-LLM: when using existing LLMs, cite the developer's reportable information or state that it was not provided.
- Protocol (14c) and registration (14d) are tagged H only, so for a pure "LLM evaluation" they are not required by the item filter, but reporting them is free credibility for a pre-registered study. [PMC12362290](https://pmc.ncbi.nlm.nih.gov/articles/PMC12362290/)

MI-CLEAR-LLM 2025 elements to copy straight into the Methods ([Europe PMC](https://europepmc.org/article/MED/41199132)):
- Model identification: name, version (ideally minor version/snapshot), developer, proprietary or open; date of access and query execution for proprietary models; training cutoff when known. The paper gives the example that an interface labelled "gpt-4o" may serve different snapshots, so state the dated snapshot and query dates.
- Access mode: web, API or local; rationale; system-level features (system prompts, memory).
- Input data type; adaptation strategy (state that weights were not altered; call the guidance summary "prompt/adaptation data", not "training").
- Prompt optimisation: steps, rationale, strategies (zero-shot, chain-of-thought, few-shot), full copy-paste text of representative prompts and, if feasible, all prompts as supplement; number of iterations and interim prompt versions.
- Prompt execution: independent calls vs constructed dialogue; share the experiment script.
- Stochasticity management: temperature and other parameters; number of attempts; method of synthesising repeats (majority vote, mean, any-of-n) and why; reliability across attempts.
- Independence of test data: any overlap with training/adaptation data; nature and source of test data; for web-sourced data, exact URLs and possible prior exposure. For synthetic items written by the GP and never published, state that they were created for the study and not posted online before the run (and the model cutoffs predate or postdate this).

CHART items most relevant ([BMJ E&E Table 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492839/)): 3a name, version identifier, release or last update date; 3b open vs closed; 5a-5b prompt development and provide prompts; 6a route of access; 6b dates and location of queries; 6c separate sessions; 6d provide all outputs; 7a ground truth definition; 7b evaluation process; 7bi number and characteristics of evaluators; 7biii whether evaluators were masked; 8 how sample size was determined; 9a statistical methods incl. reproducibility of responses; 9ai performance measures; 10a-10c alignment with ground truth, nature of deviations, harmful or misleading responses; 11a-11c interpretation, limitations, implications; 12a conflicts; 12b funding and role; 12c ethics process (12ci data privacy; 12cii copyright/licensing); 12d provide protocol; 12e where data, code and model parameters can be accessed. The CHART E&E notes synthetic data as a privacy-mitigation strategy.

AI use in writing: GAMER (BMJ Evid Based Med 2025) covers reporting of generative-AI use in producing the manuscript; JAMA Network Open requires the content, model or tool name, version and manufacturer to be described when AI-generated content is used, and says AI-generated content is discouraged outside the research design. [npj Digit Med map](https://doi.org/10.1038/s41746-025-02113-z); [JAMA Netw Open instructions, read 17 Nov 2026](https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors)

### Inferences
- The "sample size justification" item (CHART 8, TRIPOD-LLM 5/statistical) is where this study is weakest if the 48-question count was not computed: the CHART E&E example of an exploratory study justifies sample size by reference to a prior study (60 cases). Say plainly that 48 questions is a feasibility-driven exploratory size and show the bootstrap interval widths as the precision achieved.
- Because "three repeats" and "four methods x guidance on/off x 3 checkers" are the stochasticity design, state temperature (or that it was the API default and unspecified for models that fix it), repeat aggregation (all 14,688 calls analysed, or majority vote) and report between-repeat agreement. MI-CLEAR-LLM treats this as a core item.
- Cluster structure: answers are grouped by question (3 per question), so say that the bootstrap resamples whole questions to respect that clustering (already done; state it in Methods).

### Gaps
- Exact English wording of TRIPOD-LLM items not verified from the English source.
- CHART statement's own abstract checklist (16 subitems) not read.

## Q3. Pre-registration: deviations, exploratory vs confirmatory, where to register, is a git commit accepted?

### Takeaway
Report every deviation from the plan, label analyses as pre-specified or exploratory, and give the registration identifier. A git commit alone does not satisfy the usual definition of pre-registration (timestamp + registry + persistence) per FORRT, so deposit the plan on OSF (or similar) and cite the git commit hash as supporting evidence; I found no journal policy that explicitly accepts or rejects a git commit.

### Cited Findings
- OSF defines preregistration as posting a "time-stamped, read-only version of your study plan to a public repository before beginning data collection or analysis"; submitted registrations cannot be edited or deleted (can be withdrawn); changes are made via an update that "transparently reflect[s] necessary changes" and should reflect events outside your control or unexpected anomalies; OSF advises making design and analysis decisions before viewing data and describing planned and unplanned work. Page undated; read 17 Nov 2026. [OSF Help](https://help.osf.io/article/145-preregistration)
- FORRT comparison of platforms: the bare minimum for a preregistration is a timestamp, a registry and persistence; OSF and Zenodo meet all three, GitHub and AsPredicted do not (per a search summary of that page; page itself not opened). [FORRT](https://forrt.org/curated_resources/comparison-of-preregistration-platforms/)
- Willroth and Atherton, "Best Laid Plans: A Guide to Reporting Preregistration Deviations", AMPPS 7(1), Feb 2024, DOI 10.1177/25152459231213802: standard template for deviation reporting; surveyed 34 journal editors, who on average would probably support requiring it. Most deviations in published preregistered studies are unreported or reported unsystematically. [SAGE](https://journals.sagepub.com/doi/10.1177/25152459231213802)
- Metaresearch.nl (16 May 2025) argues Git version control could support "multi-stage registration" and calls this uncharted. [blog](https://metaresearch.nl/blog/2025/5/16/multi-stage-registration-a-better-way-to-pre-register)
- TRIPOD-LLM items 14c/14d ask where the protocol is available and the registry and number, or an explicit statement that it was not registered. [PMC12362290](https://pmc.ncbi.nlm.nih.gov/articles/PMC12362290/) CHART 12d asks authors to provide the study protocol. [BMJ E&E](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492839/)
- JAMA Network Open requires registration for trials only (ICMJE registry) and encourages protocols/SAPs for other designs. [JAMA Netw Open](https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors)

### Inferences
- Suggested wording: "The protocol and analysis plan were committed to a public git repository on [date] (commit [hash]) before the test run; the repository is [URL]. Because a git commit is not an independent registry timestamp, we also archived/registered the commit on [OSF/Zenodo] on [date]." If the commit was never independently timestamped, say so plainly and call the study "pre-specified" rather than "pre-registered", or deposit the commit now on OSF with the honest date and state it was deposited after the run. Do not backdate.
- Include a short deviations table (what changed, when, why, effect on results) and label every analysis as pre-specified or exploratory; the study is described as exploratory, so make clear that the primary outcomes (catch rate, false-alarm rate) were pre-specified and everything else is exploratory.

### Gaps
- No source found that states whether journals accept a git commit as pre-registration. FORRT page was seen only through a search summary.
- AsPredicted and OSF registry pages for health/LLM studies were not opened beyond the OSF help article.

## Q4. UK rules for a study with no patients and synthetic data

### Takeaway
No source says a no-participant, synthetic-data study "does not need" ethics; the route is to run the HRA "Is my study research?" tool and keep the screenshot. NHS REC review applies only where the HRA tools say so (NHS patients, staff, data or sites); a study using no participants and no NHS data is not in scope of NHS REC review. A university or employer ethics route may still be expected, and journals still ask for a statement.

### Cited Findings
- UK Policy Framework for Health and Social Care Research v3.4 (28 Apr 2026): research is "the attempt to derive generalisable or transferable new knowledge", including hypothesis-generating, methodological and descriptive research; excludes audit and service evaluation; the HRA decision tool can give a definitive answer; review by an ethics committee is needed "where their review is expected or required" (Principle 9); activities that are not research need not be managed under the framework. The framework does not address no-participant studies directly. [HRA](https://www.hra.nhs.uk/planning-and-improving-research/policies-standards-legislation/uk-policy-framework-health-social-care-research/uk-policy-framework-health-and-social-care-research/)
- "Is my study research?" tool: yes/no questions based on the Research Ethics Service's Defining Research table; result given after the questions; for review need, use the separate "Do I need NHS REC review?" tool. Page undated. [HRA tool](https://www.hra-decisiontools.org.uk/research/)
- "Do I need NHS REC review?" tool: "Not all research conducted within the UK requires review by an NHS Research Ethics Committee (REC)"; covers only NHS REC review, not other approvals; first question is "is your study research?" (NO leads to a not-research outcome); algorithm PDF v2.0 dated 4 Mar 2020; archived capture timestamp 5 May 2026. [UKGWA capture](https://tnaqa.mirrorweb.com/ukgwa/20260505155459mp_/https://hra-decisiontools.org.uk/ethics/)
- HRA proportionate review toolkit (via search summary): if the research tool says "no", no NHS/social-care ethics review is needed; HRA says a correctly completed tool outcome can be taken as authoritative. [HRA proportionate review toolkit](https://hra.nhs.uk/approvals-amendments/what-approvals-do-i-need/research-ethics-committee-review/applying-research-ethics-committee/proportionate-review-toolkit)
- Precedent wording: the CHART E&E paper states that ethics was submitted to the Hamilton Integrated Research Ethics Board and "the need for review and approval was waived (HiREB 17025)"; TRIPOD-LLM reports a COUHES IRB exemption (E-5705, 26 Mar 2024). TRIPOD-LLM item 13 asks for the name of the IRB/ethics committee and consent or waiver. [BMJ E&E](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492839/); [PMC12362290](https://pmc.ncbi.nlm.nih.gov/articles/PMC12362290/)

### Inferences
- Suggested statement (adapt to the actual tool result): "This study used no patients, no patient data and no NHS staff or sites; all clinical questions and answers were written by the investigators. Following the HRA 'Is my study research?' and 'Do I need NHS REC review?' tools (run on [date]; outputs retained), NHS REC review was not required. No consent was sought because there were no participants. The second doctor who graded a sample acted as a rater/collaborator [state whether they are an author]."
- Check one point: the second doctor and the GP are study staff, not participants, but if they are NHS employees using NHS time, local R&D/sponsor guidance may ask for a note; and the author's employer or university may want its own ethics sign-off or a "not required" email. Not covered by the HRA tools.
- Also state data protection: no personal data, so UK GDPR is not engaged.

### Gaps
- No HRA page found that addresses "synthetic data only" explicitly. The "Do I need NHS REC review?" questions beyond the first were not seen. I could not confirm whether a "not research" outcome is likely for this study (it aims to produce generalisable knowledge, so the first question probably returns "research").

## Q5. Typical length and structure of short clinical LLM papers

### Takeaway
Confirmed for JAMA Network Open only; the other journals' pages were blocked (403 or JavaScript wall) and are gaps. A research-letter format (about 800 words, 2 small tables/figures, 10 references) or an original investigation (3,000 words, 5 tables/figures, 350-word structured abstract) fits this study.

### Cited Findings
- JAMA Network Open (read 17 Nov 2026): Original Investigation up to 3,000 words, abstract up to 350 words with headings Importance, Objective, Design, Setting, Participants, Intervention(s) or Exposure(s), Main Outcome(s) and Measure(s), Results, Conclusions and Relevance; up to 5 tables and/or figures. Research Letter up to 800 words, up to 10 references, up to 2 small tables or figures, no abstract or Key Points; supplements limited to brief extra methods. EQUATOR guideline required; data sharing statement required; TRIPOD/STARD are named in its list. [JAMA Netw Open](https://jamanetwork.com/journals/jamanetworkopen/pages/instructions-for-authors)
- npj Digital Medicine published the guideline-map Comment (7 Nov 2025) as a short article; its own limits were not retrieved. [npj Digit Med](https://doi.org/10.1038/s41746-025-02113-z)

### Inferences
- Sensible short-report structure that maps to TRIPOD-LLM sections: Title naming design (LLM evaluation, classification of planted errors, synthetic questions); Abstract (Background, Methods, Results, Conclusions); Methods (items, error planting, reference standard and raters, models and dates, prompts and settings, repeats, outcomes, statistics, pre-registration and deviations, ethics); Results (one main table of catch rate and false-alarm rate with intervals, one figure); Limitations; Declarations (funding, conflicts, AI use, data and code, ethics); supplement with full prompts, items and deviations table.

### Gaps
- Word limits, abstract headings and table/figure limits for npj Digital Medicine, BMJ (Research Letter), Lancet Digital Health, NEJM AI and medRxiv were not retrieved (nature.com redirected to a cookie wall; BMJ, Lancet and NEJM AI returned 403; the medRxiv URL tried returned 404). Check each journal's current author instructions before choosing a target.

## Q6. Inter-rater agreement that is only fair to moderate

### Takeaway
Landis and Koch call kappa 0.41-0.60 moderate; McHugh (2012) calls 0.40-0.59 weak and says below 0.60 is inadequate for confident conclusions. The remedy is to report kappa with a confidence interval, percent agreement and the confusion table, explain the prevalence effect, adjudicate disagreements, and run a sensitivity analysis. Only the interpretation scales were sourced; reviewer expectations specific to LLM studies were not.

### Cited Findings
- Landis and Koch: 0.21-0.40 fair, 0.41-0.60 moderate; the scale rests on opinion. McHugh: below 0.60 indicates inadequate agreement; 0.40-0.59 weak. Kappa is low when one category is rare even if raw agreement is high. [Search summary: York kappa notes, Datanovia, Wikipedia](https://www-users.york.ac.uk/~mb55/intro/kappa4.htm)
- TRIPOD-LLM 7d and 8b require reporting rater qualifications, instructions, number of annotators, proportion double-annotated and agreement. [PMC12362290](https://pmc.ncbi.nlm.nih.gov/articles/PMC12362290/)
- CHART 7bi and 7biii require the number and characteristics of evaluators and masking; the E&E example reconciled disagreement by consulting the attending surgeon, and a separate item (10b/10c) asks for the nature of deviations and harmful responses. [BMJ E&E](https://pmc.ncbi.nlm.nih.gov/articles/PMC12492839/)

### Inferences
- Present the 0.40 as a limit of the reference standard: the labels were one GP's; a second doctor graded a blind sample and agreement was moderate at best. Report (a) kappa with a bootstrap CI and the number of items double-graded, (b) raw agreement and the 2x2 table, and prevalence-adjusted measures (PABAK or Gwet AC1) as sensitivity, (c) how disagreements were resolved (consensus or third rater) and whether the contested items were re-labelled before or after results, (d) a sensitivity analysis dropping contested items or using the second doctor's labels, and (e) a statement that catch rate and false-alarm rate are conditional on the primary rater's labels, so absolute values are uncertain even if method rankings are stable. These are my recommendations; none was confirmed as a reviewer requirement.
- Since the items were planted errors in synthetic questions, the "truth" is partly by construction (one safe, two with a single planted error); say which part of the label is by design and which part is the GP's judgement (for example, whether an error is clinically significant), because kappa is about the latter.

### Gaps
- No sources found on how clinical LLM papers or reviewers treat kappa 0.40 specifically, or on adjudication as the accepted remedy. Pages for PABAK/AC1 not retrieved.

## Sources not opened or blocked (for the writer's information)
- PMC and nature.com article pages returned captcha or redirect walls; Europe PMC REST full text was used for MI-CLEAR-LLM 2025, CHART E&E, the Korean TRIPOD-LLM translation and the npj Digit Med comment.
- BMJ, Lancet Digital Health, NEJM AI author pages returned 403; npj Digital Medicine redirected to a cookie wall.
