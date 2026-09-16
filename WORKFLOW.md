# Three Pass Workflow

## Stage 0 Research and evidence check

1. Read the professor information in the case file.
2. Confirm the professor's current institution, department, role, and research direction.
3. Review the official profile and recent publication record. Prioritize original research from the latest three to five years.
4. Select one paper that connects naturally with the candidate's previous work or emerging interests.
5. Read enough of the paper to identify:
   - the biological or clinical question;
   - the disease model and experimental system;
   - the central finding;
   - the proposed mechanism and strength of evidence;
   - at least one limitation or open question;
   - the real point of connection with the candidate.
6. Check whether the professor's direction has changed recently.
7. Save a compact evidence record in `outputs/<case-slug>_research_notes.md`.

Do not place citations or a literature review inside the outreach email. The research notes are for verification.

## Stage 1 Evidence based first draft

Write the first draft from the supplied professor information, the verified research, and the candidate profile.

The draft must have six natural paragraphs:

1. Candidate identity and reason for writing.
2. What the candidate actually did during the Master's project.
3. Research training gained and how the candidate's interest developed.
4. One specific part of the professor's recent work and why it raised a related question.
5. What the candidate can already do and what she hopes to learn during a PhD in this group.
6. A restrained closing that asks about PhD availability and mentions attachments only if they are actually supplied.

Do not label the paragraphs in the email.

### Paragraph 1 default wording

Use this wording unless the case requires a different institution, intake year, degree, or programme:

> My name is Shanshan Hao. I recently completed my Master's degree in Integrated Traditional Chinese and Western Medicine (Oncology) at Shaanxi University of Chinese Medicine, with joint research training at Zhongshan Hospital, Fudan University. I am planning to apply for PhD study at HKU for the 2027 intake, and I am writing to ask whether you expect to take on new PhD students in the coming cycle.

Do not write that the candidate is currently a Master's student.

## Stage 2 Research depth rewrite

Rewrite the first draft as a genuinely new version after checking it against the selected paper.

- Replace generic descriptions of the professor's field with one precise observation.
- Add one or at most two thoughtful questions or interpretations.
- Make clear why that point matters to the candidate's own research experience.
- Keep the connection honest when the models or mechanisms differ.
- Do not force oxidative stress, DNA damage, RAD51AP1, herbal medicine, or colorectal cancer into the email unless the connection is real.
- Do not present a paper limitation as criticism. Frame it as a question the candidate would like to understand or learn how to study.
- Use short sentences. Prefer a direct sentence over a long sentence with several clauses.

Useful patterns include:

> While my previous project used a different model, it raised a related question for me: ...

> I was particularly interested in the finding that ... It made me wonder whether ...

> This is relevant to an issue I encountered in my own work, where ...

Do not reuse these patterns mechanically. Adapt them to the evidence.

## Stage 3 Student voice polish

Rewrite the Stage 2 version once more. This third version is the final email.

The final voice should sound like a real student who has done serious laboratory work and read the professor's research carefully.

- Keep the English natural and academically accurate.
- Prefer familiar words and compact sentences.
- Vary sentence length slightly so the prose does not sound generated or rhythmic.
- Use first person where natural.
- Avoid inflated claims and excessive praise.
- Avoid a CV-style list of techniques.
- Avoid review-article language and dense mechanistic summaries.
- Avoid stock transitions such as "Furthermore," "Moreover," and "It is worth noting that."
- Preserve uncertainty. Use "may," "could," "possible involvement," or "associated with" where the evidence requires it.
- Check that the candidate still sounds willing to learn.

No system can guarantee how an AI detector will classify text. The practical target is specific, restrained, evidence-based writing without generic model-like phrasing.

## Final output format

Write `outputs/<case-slug>_email.md` in this exact order:

```markdown
# Email to Professor <Full Name>

## English version

Subject: <short specific subject>

Dear Professor <Surname>,

<six natural paragraphs>

Best regards,
Shanshan Hao

## 中文对照版

主题：<中文主题>

尊敬的<Surname>教授：

<与英文含义一致的六个自然段，不做生硬逐字翻译>

此致
敬礼
郝姗姗
```

The English section must be ready to copy and send. The Chinese section is for checking meaning. Do not insert explanations, citations, bracketed alternatives, or unresolved placeholders into either email.

## Final checklist

Confirm every item before finishing:

- The correct professor, institution, department, and intake are used.
- The salutation uses the correct surname and title.
- The email contains exactly six natural body paragraphs.
- The candidate is described as having completed the Master's degree.
- Paragraphs 2 and 3 distinguish research facts from the interest that grew from them.
- The professor section centers on one verified recent original paper.
- The paper's model, finding, and mechanism are described accurately.
- One or two questions or insights are specific and not already answered by the paper.
- No unsupported causal claim appears.
- No technique is claimed merely because it would improve matching.
- No attachment is mentioned unless it exists.
- The English is compact, natural, and student-like.
- The Chinese version preserves the English meaning and scientific caution.
- There are no citations, drafting notes, labels, or placeholders inside the email.
