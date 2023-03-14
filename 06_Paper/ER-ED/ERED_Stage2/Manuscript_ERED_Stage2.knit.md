---
title             : "Estimating individual subjective values of emotion regulation strategies"
shorttitle        : "Subjective values of emotion regulation strategies"
author:
  - name          : "Christoph Scheffel"
    orcid         : "0000-0001-5963-9229"
    affiliation   : "1"
    corresponding : yes
    address       : "Zellescher Weg 17, 01069 Dresden, Germany"
    email         : "christoph_scheffel@tu-dresden.de"
    equal_contrib : yes
    role          :         # Contributorship roles (e.g., CRediT, https://casrai.org/credit/)
      - Conceptualization
      - Methodology
      - Funding acquisition
      - Formal analysis
      - Investigation
      - Project administration
      - Software
      - Visualization
      - Writing - original draft preparation
      - Writing - review & editing
  - name          : "Josephine Zerna"
    orcid         : "0000-0003-2892-884X"
    affiliation   : "1"
    equal_contrib : yes
    role          :
      - Conceptualization
      - Methodology
      - Funding acquisition
      - Investigation
      - Project administration
      - Software
      - Visualization
      - Writing - review & editing
  - name          : "Anne Gärtner"
    orcid         : "0000-0003-4296-963X"
    affiliation   : "1"
    role          :
      - Formal analysis
      - Writing - review & editing
  - name          : "Denise Dörfel"
    orcid         :
    affiliation   : "1"
    role          :
      - Conceptuatlization
      - Writing - review & editing
  - name          : "Alexander Strobel"
    orcid         : "0000-0002-9426-5397"
    affiliation   : "1"
    role          :
      - Conceptualization
      - Methodology
      - Writing - review & editing 
affiliation       :
  - id            : "1"
    institution   : "Faculty of Psychology, Technische Universität Dresden, 01069 Dresden, Germany"
authornote        :
abstract          : |
 Individuals have a repertoire of emotion regulation (ER) strategies at their disposal, which they can use more or less flexibly. 
 In ER flexibility research, strategies that facilitate goal achievement are considered adaptive and therefore are subjectively valuable. 
 Individuals are motivated to reduce their emotional arousal effectively and to avoid cognitive effort. 
 Perceived costs of ER strategies in the form of effort, however, are highly subjective. 
 Subjective values (SVs) should therefore represent a trade-off between effectiveness and subjectively required cognitive effort. 
 However, SVs of ER strategies have not been determined so far. 
 We present a paradigm that is suitable for determining individual SVs of ER strategies. 
 Using a multilevel modelling approach, it will be investigated whether individual SVs can be explained by effectiveness (subjective arousal, facial muscle activity) and subjective effort. 
 Relations of SVs to personality traits will be explored.
keywords          : "emotion regulation, regulatory effort, effort discounting, registered report, specification curve analysis"
wordcount         : "XXXXX"
bibliography      : ["ER_ED.bib"]
floatsintext      : yes
figsintext        : yes
figurelist        : no
tablelist         : no
footnotelist      : no
linenumbers       : yes
mask              : no
draft             : no
documentclass     : "apa6"
classoption       : "man"
output            : papaja::apa6_pdf
csl               : nature.csl
header-includes   :
    - \usepackage{booktabs}
    - \usepackage{longtable}
    - \usepackage{array}
    - \usepackage{multirow}
    - \usepackage{wrapfig}
    - \usepackage{float}
    - \usepackage{colortbl}
    - \usepackage{pdflscape}
    - \usepackage{tabu}
    - \usepackage{threeparttable}
    - \usepackage{threeparttablex}
    - \usepackage[normalem]{ulem}
    - \usepackage{makecell}
    - \usepackage{xcolor}
    - \usepackage{setspace}\doublespacing
    - \usepackage[final]{pdfpages}
    - \usepackage{chngcntr}
editor_options: 
  markdown: 
    wrap: sentence
---

```{=tex}
\renewcommand\thesection{\Alph{section}}
\counterwithout{figure}{section}
\setcounter{figure}{0}
```

------------------------------------------------------------------------












# 1. Introduction

The ability to modify emotional experiences, expressions, and physiological reactions [@Gross1998antecedent] to regulate emotions is an important cognitive skill. 
It is therefore not surprising that emotion regulation (ER) has substantial implications for well-being and adaptive functioning[@Gross1998emerging].
Different strategies can be used to regulate emotions, namely situation selection, situation modification, attentional deployment, cognitive change, and response modification[@Gross1998antecedent], and, following the taxonomy of Powers and LaBar[-@Powers2019], individuals can implement ER strategies by means of different tactics.
So called antecedent-focused strategies, e.g., attentional deployment and cognitive change, take effect early in the emotion generation process[@Gross1998antecedent].
In contrast, response modification takes place late in the process and is therefore conceptualized as a response-focused strategy[@Gross1998antecedent].
This postulated temporal sequence of ER strategies influences their effectiveness.
Albeit it is meta-analytically proven that all mentioned strategies reduce subjective emotional experience, distraction as a tactic of attentional deployment and (expressive) suppression as a tactic of response modulation showed only small to medium effect sizes (distraction: _d~+~_ = 0.27; suppression: _d~+~_ = 0.27).
In contrast, distancing as tactic of cognitive change showed the highest effectiveness with an effect size of _d~+~_ = 0.45[@Webb2012].

Psychophysiological measures provide further important information on the effectiveness of emotion regulation strategies (for an overview, see Zaehringer et al.[@Zaehringer2020]).
Compared to cardiovascular, electrodermal, and pupillometric autonomic responses, facial electromyography has been reported consistently across studies to be influenced by emotion regulation with even medium effect sizes.
For example, studies have shown that reappraisal of negative emotion is associated with reduced activity of the corrugator supercilii (associated with anger, sadness, and fear) with _d~-~_ = 0.32[@Zaehringer2020].
In addition, the levator labii superioris (associated with disgust) has also been associated with reduced activity during reappraisal[@Burr2021]. 
Similar effects have been reported for suppression[@Burr2021], distancing[@Gaertner2021], and distraction[@Schoenfelder2014].
Importantly, results on electromyographic measures  seem to be more consistent compared to other autonomic measures, likely because they are specific to emotional valence and its changes.

Similarly to the differences in short term effectiveness, these tactics from three different strategies are also related to different medium and long-term consequences. 
In particular, strategies that do not change the emotional content of the situation, for instance by taking a neutral perspective (i.e., distraction and suppression) are presumed to be disadvantageous in the longer term.
Thus, the self-reported habitual use of suppression is associated with more negative affect and lower general well-being[@GrossJohn2003]. 
In addition, a number of ER strategies, e.g., rumination and suppression, have been associated with mental disorders (for meta-analytic review, see Aldao et al.[@Aldao2010]), which led to the postulation of *adaptive* (such as reappraisal, acceptance) and *maladaptive* (such as suppression, rumination) ER strategies.
For example, it was shown that maladaptive ER strategies (rumination and suppression) mediate the effect between neuroticism and depressive symptoms[@Yoon2013].

The postulation of *adaptive* and *maladaptive* ER strategies has been challenged by the concepts of ER repertoire and ER flexibility.
Within this framework, *maladaptive*  refers to inflexible ER strategy use or use of strategies that are hindering goal achievement[@Aldao2015].
Adaptive flexible ER requires a large repertoire of ER strategies[@Aldao2015].
The term “repertoire” can be defined as the ability to utilize a wide range of regulatory strategies in divergent contextual demands and opportunities[@Bonanno2013].
A growing number of studies report findings about the repertoire of emotion regulation strategies and its relationship to psychopathology[@DixonGordon2015;@Lougheed2012;@Southward2018]. 
Additionally, greater ER flexibility is related to reduced negative affect and therefore beneficial in daily life[@Blanke2020].

How do people choose strategies from their repertoire? 
Similarly to the expectancy-value model of emotion regulation[@Tamir2015] it could be assumed, that people also assign a value to an ER strategy reflecting the usefulness of this strategy for goal achieving.
Evidence from other psychological domains (e.g., intertemporal choice[@Kable2007]) shows that subjective values (SVs) are attributed to the choice options on the basis of which the decision is made. 
Research on ER choice has identified numerous factors that influence the choice of ER strategies, which can be seen as indirect evidence for factors influencing SVs[@Sheppes2014]. 
For example, a study found that the intensity of a stimulus or situation plays a role in the choice[@Sheppes2011]. 
Higher intensity of the (negative) stimulus lead to a choice of rather disengaging tactics of attentional deployment, like distraction[@Sheppes2011;@Sheppes2014].
ER choice was further influenced by, among others, extrinsic motivation (e.g., monetary incentives), motivational determinants (i.e., hedonic regulatory goals), and effort[@Sheppes2014;@Scheffel2021].
Nonetheless, there are only few studies to date that examined the required effort of several strategies in more detail and compared them with each other.
Furthermore, the research on ER choice lacks information regarding the strategies that were *not* chosen in each case.
It is unclear whether people had clear preferences or whether the choice options were similarly attractive.

We assume that people choose the strategy that has the highest value for them at the moment.
The value is determined against the background of goal achievement in the specific situation: A strategy is highly valued if it facilitates goal achievement[@Aldao2015]. 
One certainly central goal is the regulation of negative affect.
The effectiveness of ER strategies should therefore influence the respective SV.
A second, intrinsic, and less obvious goal is the avoidance of effort[@Inzlicht2018].
When given the choice, most individuals prefer tasks that are less effortful[@Hull1943].
Cognitive effort avoidance has been reported in many contexts, for example in affective context[@Gonzalez-Garcia2021], the context of decision making[@Kool2010], and executive functions[@Cheval2020], and is associated with Need for Cognition (NFC)[@Cacioppo1982], a stable measure of the individual pursuit and enjoyment of cognitive effort[@Westbrook2013;@Strobel2020].
In the area of emotion regulation, too, there are initial indications that people show a tendency towards effort avoidance.
Across two studies, we could show in previous work that the choice for an ER strategy is mainly influenced by the effort required to implement a given strategy[@Scheffel2021].
In our studies, participants used the strategies distancing and suppression while inspecting emotional pictures.
Afterwards, they choose which strategy they wanted to use again.
Participants tended to re-apply the strategy that was subjectively less effortful, even though it was subjectively not the most effective one - in this case: suppression.
Moreover, the majority of participants stated afterwards the main reason for their choice was effort.
We assume therefore that, although individuals trade off both factors - effectiveness and effort - against each other, effort should be the more important predictor for SVs of ER strategies.
In addition, perceived utility should have an impact on SVs. 
A strategy that is less effortful and can objectively regulate arousal (i.e., is effective), but is not subjectively perceived as useful, should have a low SV.
SVs of ER Strategies could therefore be helpful to describe the ER repertoire[@Aldao2015] more comprehensively.
Depending on the flexibility of a person, different patterns of SVs could be conceivable: A person with high flexibility would show relatively high SVs for a number of strategies.
This would mean that all strategies are a good option for goal achievement.
A second person with less flexibility, however, would show high SVs only for one strategy or low SVs for all of the strategies.
This in turn would mean that there is only a limited amount of strategies in the repertoire to choose from. 
Subsequently, the ability to choose an appropriate strategy for a specific situation is also limited.

So far we have not seen any attempt in ER choice research to determine individual SVs of ER strategies.
However, this would be useful to describe interindividual differences in the preference of ER strategies and the ER repertoire more comprehensively.
To investigate this question, the individual SVs of each strategy available for selection would have to be determined.
Promising approaches can be found in studies on difficulty levels of effortful cognitive tasks.  
Individual SVs of effortful cognitive tasks have been quantified using the Cognitive Effort Discounting Paradigm (COG-ED)[@Westbrook2013]. 

In the original study by Westbrook et al.[-@Westbrook2013], cognitive load was varied using the *n*-back task, a working memory task that requires fast and accurate responses to sequentially presented stimuli. 
Participants had to decide in an iterative procedure whether they wanted to repeat a higher *n*-back level for a larger, fixed monetary reward, or a lower level for a smaller, varying reward, with the implicit assumption that the objectively easiest *n*-back level has the highest SV.
In the present study, we want to use this paradigm to determine SVs of ER strategies.
In doing so, we need to make an important change: We have to adapt the assumption that the easiest *n*-back level has the highest SV.
As we have shown in previous studies, there are large inter-individual differences in the preference and perceived subjective effort of ER strategies[@Scheffel2021].
Moreover, there is nothing like an objectively easiest ER strategy.
It could be assumed, that the antecedent-focused strategies, i.e. attentional deployment and cognitive change, require less effort, because according to Gross[-@Gross1998antecedent] these strategies apply when the emotional reaction has not fully developed, yet. 
In contrast, suppression would need ongoing effort, because it takes effect late in the emotion generating process and does not alter the emotion itself. 
A similar assumption has been made by Mesmer-Magnus et al.[-@MesmerMagnus2012], who state that Surface Acting (the equivalent to expressive suppression in emotional labor research) is supposed to continuously require high levels of energy (hence effort). 
Deep Acting (which refers to reappraisal), in turn, only initially needs the use of energy. 
This would be in conflict with findings in our previous studies, that showed that many people choose expressive suppression because they evaluated it as less effortful, hence easy[@Scheffel2021].
Others define emotion regulation on a continuum from explicit, conscious, and effortful to implicit, unconscious, automatic and effortless[@Gyurak2011].
This would mean, that all explicit strategies that have been proposed by the process model of emotion regulation are similarly effortful[@Gross1998antecedent].
Similarly, the flexibility approach of emotion regulation also states, that there is no "best" strategy[@Gross2015].
An emotion regulation attempt is adaptive, when the intended, individual goal is reached. Those attempts could also consist of sequences of regulatory efforts using different strategies, which might be effective and effortless only in this specific context.
Therefore, we have to add an additional step, which precedes the other steps and where the ER option with the higher subjective value is determined. 
In this step, the same monetary value (i.e., 1 €) is assigned to both options.
The assumption is that participants now choose the option that has the higher SV for them.
In the next step we return to the original paradigm.
The higher monetary value (i.e., 2 €) is assigned to the option that was not chosen in the first step and therefore is assumed to have the lower SV.
In the following steps, the lower value is changed in every iteration according to Westbrook et al.[-@Westbrook2013] until the indifference point is reached.
This procedure will be repeated until all strategies have been compared.
The SV of each strategy is calculated as the mean of this strategy's SV from all comparisons.
In case a participant has a clear preference for one strategy, the SV of this strategy will be 1.
But our paradigm can also account for the case that a person does not have a clear preference.
Then no SV will be 1, but still, the SVs of all strategies can be interpreted as absolute values and in relation to the other strategy's SVs (see Figure \@ref(fig:ResponsePatterns)).
In a separate study, we will test our adapted paradigm together with a *n*-back task and explore whether this paradigm can describe individuals that do not prefer the easiest *n*-back option (see Zerna, Scheffel et al.[@ZernaScheffel2022]).

[INSERT FIGURE 1 HERE]

\begin{figure}
\includegraphics[width=\textwidth]{figures/Paradigm_Scheme_T2} \caption{Exemplary visualization of two response patterns. In the top half, the person has a clear preference for one of the three strategies. In the lower half, they have no clear preference and therefore show an inconsistent response pattern. This pattern can be represented by our paradigm. Figure available at https://osf.io/vnj8x/, under a CC-BY4.0 license.}(\#fig:ResponsePatterns)
\end{figure}

The aim of the present study is to evaluate whether this paradigm is suitable for determining SVs of ER strategies. 
As a manipulation check, we first want to investigate whether the valence of the pictures is affecting subjective and physiological responding, resulting in lower subjective arousal ratings after and lower EMG activity during neutral compared to negative pictures.
Second, we want to check whether the ER strategies distraction, distancing, and suppression effectively reduce subjective arousal and physiological responding compared to the active viewing condition.
Third, we want to see whether the strategies subjectively require more cognitive effort than the active viewing condition, and whether participants re-apply the for them least effortful strategy. 
Furthermore, we want to investigate whether subjective effort, arousal ratings, subjective utility, and EMG activity predict individual subjective values of ER strategies.
And lastly, we want to check whether the SV of a strategy is associated with its likelihood of being chosen again, and whether SVs reflect participants' self-reported ER flexibility.
All hypotheses are detailed in the [design table](#DesignTable).
Exploratorily, we want to investigate whether individual SVs are related to personality traits and how individual SVs of ER strategies relate to SVs of other tasks with different demand levels, namely *n*-back.

















# 2. Method

We report how we determined our sample size, all data exclusions (if any), all manipulations, and all measures in the study[@Simmons2012].
The paradigm was written and presented using *PsychoPy*[@Peirce2019].
We used *R* with *R Studio*[@RCore2021; @RStudioTeam2020] with the main packages *afex*[@Singmann2021] and *BayesFactor*[@Morey2021] for all analyses.
The R Markdown file used to analyze the data and write this document, as well as the raw data and the materials are freely available at https://github.com/ChScheffel/CAD.
A complete list of all measures assessed in the study can be found at OSF (<https://osf.io/vnj8x/>) and GitHub (https://github.com/ChScheffel/CAD).

## 2.1 Ethics information

The study protocol complies with all relevant ethical regulations and was approved by the ethics committee of the Technische Universität Dresden (reference number EK50012022). 
Prior to testing, written informed consent was obtained.
Participants received 24€ in total or course credit for participation.

## 2.2 Pilot data

The newly developed ER paradigm was tested in a pilot study with $N=16$ participants (9 female; age: $M = 24.1\text{ }\pm\text{ }SD = 3.6$).
Regarding self-reported arousal, results showed significant higher subjective arousal for active viewing of negative compared to neutral pictures.
However, ER strategies did not lead to a reduction of subjective arousal compared to active viewing of negative pictures.
Regarding physiological responses, ER strategies were associated with reduced facial muscle activity of the *corrugator* and *levator* compared to active viewing of negative pictures.
In accordance with our previous study[@Scheffel2021], we found that the use of ER strategies compared to active viewing was associated with increased subjective effort.
All results are detailed in the OSF repository (<https://osf.io/vnj8x/>).

## 2.3 Design

Young healthy participants (aged 18 to 30 years) were recruited using the software *ORSEE*[@Greiner2015] at the Technische Universität Dresden.
Participants were excluded from participation if they do not fluently speak German, had current or a history of psychological disorders or neurological trauma, or reported to take medication.
Participants were invited to complete an online survey containing different questionnaires to assess broad and narrow personality traits and measures of well-being.
The study consisted of two lab sessions, which took place in a shielded cabin with constant lighting.
Before each session, participants received information about the respective experimental procedure and provided informed consent.
In the first session participants filled out a demographic questionnaire and completed an *n*-back task with the levels one to four.
Then, they completed an effort discounting (ED) procedure regarding the *n*-back levels on screen, followed by a random repetition of one *n*-back level [@ZernaScheffel2022].
The second session took place exactly one week after session one.
Participants provided informed consent and received written instructions on the ER paradigm and ER strategies that they should apply.
A brief training ensured that all participants were able to implement the ER strategies.
Next, electrodes to measure facial EMG were attached and the ER task was conducted, followed by an ED procedure regarding the ER strategies.
After that, participants chose one ER strategy to repeat one more time.
Study data were collected and managed using REDCap electronic data capture tools hosted at Technische Universität Dresden[@Harris2009; @Harris2019].

### 2.3.1 Psychometric measures

The online survey contained a number of questionnaires. 
In the focus of the current project was the Flexible Emotion Regulation Scale (FlexER)[@Doerfel2019].  
It assesses flexible use of ER strategies with items such as "If I want to feel less negative emotions, I have several strategies to achieve this.", which we define as ER flexibility. 
The items were rated on a 4-point scale ranging from "strongly agree" to "strongly disagree".

Further psychological constructs were assessed but had no clear hypotheses in the present work and are therefore investigated only exploratory:
General psychological well-being was assessed using the German version of the WHO-5 scale[@Bech2004; @Braehler2007].
To measure resilience, the German version 10-item-form of the Connor-Davidson resilience Scale (CD-RISC)[@Connor2003; @Campbell-Sills2007; @Sarubin2015] was used.
Habitual use of ER will was assessed using the German version of the Emotion Regulation Questionnaire (ERQ)[@GrossJohn2003; @Abler2009].
Implicit theories of willpower in emotion control was assessed using the implicit theories questionnaire from Bernecker and Job[@Bernecker2017].
To assess Need for Cognition, the German version short form of the Need for Cognition Scale[@Cacioppo1982; @Bless1994] was used.
To assess self-control [@Paschke2016], sum scores of the German versions of the following questionnaires were used: the Self-Regulation Scale (SRS)[@Schwarzer1999], the Brief Self-Control Scale (BSCS)[@Tangney2004; @Sproesser2011], and the Barratt Impulsiveness Scale (BIS-11)[@Patton1995; @Hartmann2011].
Attentional control were assessed using the Attentional Control Scale (ACS)[@Derryberry2002].
For more detailed information on psychometric properties of the questionnaires, please see [supplementary material](#SupplementQuestionnaires). 

### 2.3.2 Emotion regulation paradigm

The ER paradigm consisted of three parts that will be described in the following.

*Part one: ER task.* <br> Part one was a standard ER task in a block design (see Figure \@ref(fig:DesignERED)), similar to paradigms previously used by our group[@Scheffel2021].
Participants were told to actively view neutral and negative pictures (see [2.3.3](##stimuli)) or to regulate all upcoming emotions by means of distraction, distancing, and expressive suppression, respectively.
Every participant first had the condition "active viewing-neutral" that served as a baseline condition.
During this block, 20 neutral pictures were presented.
Participants were asked to "actively view all pictures and permit all emotions that may arise." 
In the second block, participants actively viewed negative pictures.
During the third, fourth, and fifth block, participants saw negative pictures and were asked to regulate their emotions using distraction, distancing, and suppression.
In order to achieve distraction, participants were asked to think of a geometric object or an everyday activity, like brushing their teeth.
During distancing, participants were asked to "take the position of a non-involved observer, thinking about the picture in a neutral way." 
Participants were told not to re-interpret the situation or attaching a different meaning to the situation.
During suppression, participants were told to "suppress their emotional facial expression." 
They should imagine being observed by a third person that should not be able to tell by looking at the facial expression whether the person is looking at an emotional picture.
Participants were instructed not to suppress their thoughts or change their facial expression to the opposite[@Scheffel2021].
All participants received written instruction and completed a training session.
After the training session, participants were asked about their applied ER strategies to avoid misapplication.
The order of the three regulation blocks (distraction, distancing, and suppression) were randomized between participants.
Each of the blocks consisted of 20 trials showing neutral (Block 1) and negative (Blocks 2, 3, 4, 5) pictures.
Each trial began with a fixation cross that lasted 3 to 5 seconds (random uniform distributed).
It was followed by neutral or negative pictures for a total of 6 seconds.
After each block, participants retrospectively rated their subjective emotional arousal ("not at all aroused" to "very highly aroused"), their subjective effort ("not very exhausting" to "very exhausting"), and - after the regulation blocks - the utility of the respective strategy ("not useful at all" to "very useful") on a continuous scale using a slider on screen.

*Part two: ER effort discounting.* <br> In the second part, ER effort discounting took place.
The procedure of the discounting will follow the COG-ED paradigm by Westbrook et al.[-@Westbrook2013] with a major change.
We used the following adaption that allowed the computation of SVs for different strategies without presuming that all individuals would inherently evaluate the same strategy as the easiest one: For each possible pairing (distraction vs. distancing, distraction vs. suppression, and distancing vs. suppression), each of the two strategies were presented with a monetary reward.
Because there is no strategy that is objectively more difficult, we added initial comparisons asking the participants to choose between "1€ for strategy A or 1€ for strategy B".
They decided by clicking the on-screen button of the respective option.
Each of the three strategy pairs were presented three times in total, in a randomized order and randomly assigned which strategy appeared on the left or right side of the screen.
For each pair, the strategy that was chosen at least two out of three times was assigned the flexible starting value of 1€, the other strategy was assigned the fixed value of 2€.
After this, comparisons between strategies followed the original COG-ED paradigm[@Westbrook2013].
Each pairing was presented six consecutive times, and with each decision the reward of the strategy with the starting value of 1€ was either lowered (if this strategy was chosen) or raised (if the strategy with the fixed 2€ reward was chosen).
The adjustment started at 0.50€ and each was half the adjustment of the previous step, rounded to two digits after the decimal point.
If a participant always chose the strategy with the fixed 2€ reward, the other strategy's last value on display was 1.97€, if they always choose the lower strategy, its last value was 0.03€.
The sixth adjustment of 0.02€ was done during data analysis, based on the participants' decision in the last display of the pairing.
Participants were instructed to decide as realistically as possible by imagining that the monetary reward was actually available for choice.

*Part three: ER choice.* <br> After the discounting part, participants chose which one of the three ER strategies (distraction, distancing or suppression) they wanted to re-apply.
Importantly, there was no further instruction on what basis they should make their decision.
Participants should make their decision freely, according to criteria they consider important for themselves.
However, participants were asked to state the reasons for the decision afterwards in RedCap using a free text field.
As soon as they have decided, they saw the respective instruction and the block with another 20 negative pictures started.

[INSERT FIGURE 2 HERE]

\begin{figure}
\includegraphics[width=\textwidth]{figures/Design_ER-ED} \caption{Block design of the paradigm. Every participant starts with two "active viewing" blocks continaing neutral (Block 1) and negative (Block 2) pictures. Order of the regulation blocks (Blocks 3, 4, and 5) was randomized between participants. After, the discounting procedure took place. All three regulation strategies were compared pairwise. Before the last block, participants could decide which regulation strategy they wanted to reapply. Subjective arousal and effort ratings were assessed after each block using a slider on screen with a continuous scale. Figure available at https://osf.io/vnj8x/, under a CC-BY4.0 license.}(\#fig:DesignERED)
\end{figure}

### 2.3.3 Stimuli

Pictures that were used in the paradigm were selected from the Emotional Picture Set (EmoPicS) [@Wessa2010] and the International Affective Picture System (IAPS)[@Lang2008].
The 20 neutral pictures (Valence (V): *M* $\pm$ *SD* = 4.81 $\pm$ 0.51; Arousal (A): *M* $\pm$ *SD* = 3 $\pm$ 0.65) depicted content related to the categories persons, objects, and scenes.
Further, 100 negative pictures, featuring categories animals, body, disaster, disgust, injury, suffering, violence, and weapons, were used.
An evolutionary algorithm [@Yu2010] was used to cluster these pictures into five sets with comparable valence and arousal values (set one: V: *M* $\pm$ *SD* = 2.84 $\pm$ 0.57, A: *M* $\pm$ *SD* = 5.62 $\pm$ 0.34; set two: V: *M* $\pm$ *SD* = 2.64 $\pm$ 0.46, A: *M* $\pm$ *SD* = 5.58 $\pm$ 0.35; set three: V: *M* $\pm$ *SD* = 2.82 $\pm$ 0.62, A: *M* $\pm$ *SD* = 5.60 $\pm$ 0.39; set four: V: *M* $\pm$ *SD* = 2.65 $\pm$ 0.75, A: *M* $\pm$ *SD* = 5.61 $\pm$ 0.41; set five: V: *M* $\pm$ *SD* = 2.74 $\pm$ 0.70, A: *M* $\pm$ *SD* = 5.63 $\pm$ 0.37).
A complete list of all pictures and their classification into sets can be found in supplementary material table S1.
The five sets of negative pictures were assigned randomly to the blocks.

### 2.3.4 Facial electromyography

Bipolar facial electromyography (EMG) were measured for *corrugator supercilii* and *levator labii* as indices of affective valence[@Bradley2000], similar to previous work by our group[@Gaertner2021].
Two passive surface Ag/AgCl electrodes (8 mm inner diameter, 10 mm distance between electrodes) were placed over each left muscle according to the guidelines of Fridlund and Cacioppo[@Fridlund1986].
The ground electrode was placed over the left *Mastoid*.
Before electrode placement, the skin was abraded with Every abrasive paste, cleaned with alcohol, and filled with Lectron III electrolyte gel.
Raw signals were amplified by a BrainAmp amplifier (Brain Products Inc., Gilching, Germany).
Impedance level were kept below 10 $k\Omega$. 
Data were sampled at 1000 Hz, filtered, rectified and integrated. 
A 20 Hz high pass (order 8), a 300 Hz low pass (order 8), and a 50 Hz notch filter was applied to both signals.
*Corrugator* and *levator* EMG was analyzed during the 6 s of picture presentation.
EMG data were baseline-corrected using a time window of 2 s prior to stimulus onset [@Bradley2000]. 
Last, the sampling rate was changed to 100 Hz, and EMG data were averaged for each condition and each participant.

## 2.4 Sampling plan

Sample size calculation was done using *G\*Power*[@Faul2007; @Faul2009].
In a meta-analysis of Zaehringer and colleagues[-@Zaehringer2020], effect sizes of ER on peripheral-physiological measures were reported:
To find an effect of $d=-0.32$ of ER on *corrugator* muscle activity with $\alpha=.05$ and $\beta=.95$, data of at least $N=85$ have to be analyzed.
Power analyses of all other hypotheses yielded smaller sample sizes.
However, if participants withdraw from study participation, technical failures occur, or experimenter considers the participant for not suitable for study participation (e.g., because the participant does not follow instructions or shows great fatigue), respective data will also be excluded from further analyses.
Therefore, we aimed to collect data of $N=120$ participants, about $50%$ more data sets, than necessary.
Detailed information on power calculation for each hypothesis can be found in the [design table](#DesignTable).

## 2.5 Analysis plan

Data collection and analysis were not performed blind to the conditions of the experiments.
Data of whole participants were excluded from analysis if participants withdraw their consent or they stated that they did not follow experimental instructions.
EMG data of subjects were excluded from analysis if errors occured during recording.
No further data exclusions were planned.
The level of significance was set to $\alpha=.05$.
For hypotheses H1-4, repeated measures analysis of variance (rmANOVA) were conducted and estimated marginal means were computed using the *afex* package[@Singmann2021].
Greenhouse-Geisser-corrected degrees of freedom and associated $p$-values were reported when the assumption of sphericity was violated.
If the within-subjects factor of interest was significant, pairwise contrasts were calculated using Bonferroni adjustment for multiple testing.
Proportion of explained variance $\eta_{p}^{2}$ was reported as a measure of effect size.

*Effect of valence on arousal and facial EMG.*<br> 
To examine the impact of valence of emotional pictures on subjective arousal ratings (H1a), a rmANOVA with the factor valence (neutral and negative) for the strategy active viewing was conducted.
To examine the impact of valence on physiolocigal responding (H1b and H1c), a rmANOVA with the factor valence (neutral and negative) for the strategy active viewing was conducted for EMG *corrugator* and *levator* activity.

*Effects of emotion regulation on arousal, facial EMG, and effort.* <br> 
To investigate the effects of the three ER strategies on subjective arousal (H2a), another rmANOVA  with the factor strategy (active viewing - negative, distraction, distancing, and suppression) for subjective arousal ratings was conducted.
To examine the effects of the three ER strategies on physiological responding (H3a and H3b), another rmANOVA with the factor strategy (active viewing - negative, distraction, distancing, and suppression) for EMG *corrugator* and *levator* activity was conducted.
To examine the effect of ER strategies on subjective effort (H4a), a rmANOVA with the factor strategy (active viewing - negative, distraction, distancing, and suppression) for subjective effort ratings was conducted.

*Subjective values of emotion regulation strategies.* <br> For each ER strategy, SVs were calculated as follows: first, the value 0.02€ was added to or subtracted from the last monetary value of the flexible strategy, depending on the participant's last choice.
Second, to obtain the SV of the fixed strategy (the minimum relative reward required for participants to choose the flexible over the fixed strategy), the last value of the flexible strategy was divided by 2€.
Therefore, the SVs of the flexible strategies were 1, because they were chosen in the initial comparison of each pairing in which the same value was offered for both strategies, so they were the preferred strategy of each pairing.
The SVs of the fixed strategies lay between 0 and 1, with lower values indicating that the participant would need a much higher monetary incentive to choose this strategy over the other one in the pairing. 
The final SV per strategy for each participant was computed by averaging the SVs of each strategy across pairings.

To explore the association between subjective effort (H5a), subjective arousal (H5b), subjective utility (H5c), and physiological responding (H5d,e) on SVs, a multilevel model (MLM) was specified using the $lmerTest$ package[@Kuznetsova2017].
First, ER strategies were recoded and centered for each subject according to their individual SVs: The strategy with the highest SV will be coded as -1, the strategy with the second highest SV 0, and the strategy with the lowest SV will be coded as 1.
Restricted maximum likelihood (REML) was applied to fit the model.
A random slopes model of SVs including subjective effort (effort ratings), subjective arousal (arousal ratings), utility (utility ratings), and physiological responses (*corrugator* and *levator* activity) as level-1-predictors was specified.
$$
\begin{split}
SV \sim strategy\ + \text{effort rating} + \text{arousal rating} + \text{utility rating} + corrugator \text{ activity} \\\ + levator \text{ activity} + (strategy|subject)
\end{split}
$$ 
Level-1-predictors were centered within cluster[@Enders2007].
Residuals of the final model were inspected visually.
Intraclass correlation coefficient (ICC), $\rho$, was reported for each model (null model, as well as full model).
The presented MLM followed the conceptualization of Zerna, Scheffel, et al.[@ZernaScheffel2022]

To investigate whether individual SVs predict ER choice (H7a), a $\chi{2}$ test with predicted choice (highest SV of each participant) and actual choice was computed.
Furthermore, an ordinal logistic regression with the dependent variable choice and independent variables SVs of each strategy was computed.

The association between flexible ER and SVs of ER strategies (H7b) was investigated with a linear regression using the individual $intercept$ and $slope$ of each participants' SVs to predict their FlexER score.
To this end, for each participant, SVs were sorted by magnitude in descending order and entered as dependent variable in a linear model, with strategy (centered, i.e., -1, 0, 1) as independent variable.
The resulting $intercept$ informs about the extent to which an individual considers any or all of the ER strategies as useful for regulation their emotion, while the $slope$ informs about the flexibility in the use of emotion regulation strategies. 
The individual intercepts and slopes were entered as predictors in a regression model with the FlexER score as dependent variable. 
A positive association with the predictor $intercept$ would indicate that overall higher SVs attached to ER strategies predicts higher scores on the FlexER scale. 
A positive association with the predictor $slope$ would indicate that less negative slopes, i.e., a smaller preference for a given ER strategy, would be associated with a higher score of the FlexER scale.

The influence of personality traits on SVs were investigated exploratorily.
Therefore, the MLM specified above was extended by the level-2-predictors NFC and self-control.

For each result of the analyses, both $p$-values and Bayes factors $BF10$, calculated using the *BayesFactor* package[@Morey2021], were reported. 
Bayes factors were calculated using the default prior widths of the functions *anovaBF*, *lmBF* and *regressionBF*.

## Data availability

The data of this study can be downloaded from [osf.io/vnj8x/](https://osf.io/vnj8x/).

## Code availability

The paradigm code, the R script for analysis, and the R Markdown file used to compile this document are available at [osf.io/vnj8x/](https://osf.io/vnj8x/).

## Protocol registration

The Stage 1 Registered Report protocol has been approved and is available at [osf.io/d6sc9/](https://osf.io/d6sc9/).










# 3. Results

## 3.1 Participants and descriptive statistics

Data collection took place between 2022-08 and 2023-02.
A total of $N=151$ participants completed the online survey and were invited to participate in the two lab sessions.
Of these, $N=125$ participated in the first laboratory session [@ZernaScheffel2022] and $N=121$ completed the second laboratory session.
Of these, $n=1$ person had to be excluded from analyses because they did not follow the instructions.
The final sample consisted of $N=120$ participants (100 female; age: $M=22.5\text{ }\pm\text{ }SD = 3.0$).
Please note that sample size for individual calculations may be smaller due to failure of EMG recording ($n=1$) and failure to record utility ratings ($n=18$).

## 3.2. Confirmatory analyses

### Manipulation checks

#### Subjective arousal and physiological responding

To explore whether negative pictures evoke emotional arousal and physiological responding, we conducted separate ANOVAs for the active viewing condition with predictors subjective arousal, *Corrugator* and *Levator* activity. 
We found a highly significant main effect of valence for subjective arousal ($F(1, 119) = 399.95$, $p < .001$, $\hat{\eta}^2_G = .589$, 90\% CI $[.498, .659]$, $\mathrm{BF}_{\textrm{10}} = 1.47 \times 10^{44}$), *Corrugator* activity ($F(1, 117) = 27.73$, $p < .001$, $\hat{\eta}^2_G = .111$, 90\% CI $[.037, .206]$, $\mathrm{BF}_{\textrm{10}} = 8.67 \times 10^{16}$), and *Levator* activity ($F(1, 117) = 8.87$, $p = .004$, $\hat{\eta}^2_G = .039$, 90\% CI $[.002, .111]$, $\mathrm{BF}_{\textrm{10}} = 188.72$), indicating that negative pictures successfully evoked emotional arousal and physiological responding.<!--JZ: Am besten auch die Richtung angeben, also "...valence for an increase in subjective..."-->

To investigate whether ER strategies reduce emotional arousal and physiological responding, we conducted separate rmANOVA comparing subjective arousal, *Corrugator* and *Levator* activity of four strategies (active viewing, distraction, distancing, suppression). 
We found a significant effect of strategy for subjective arousal ($F(2.71, 322.55) = 7.39$, $p < .001$, $\hat{\eta}^2_G = .015$, 90\% CI $[.000, .036]$, $\mathrm{BF}_{\textrm{10}} = 0.21$), *Corrugator* activity ($F(1.76, 206.02) = 13.70$, $p < .001$, $\hat{\eta}^2_G = .056$, 90\% CI $[.019, .094]$, $\mathrm{BF}_{\textrm{10}} = 6.16 \times 10^{7}$), and *Levator* activity ($F(1.54, 180.41) = 19.95$, $p < .001$, $\hat{\eta}^2_G = .089$, 90\% CI $[.043, .134]$, $\mathrm{BF}_{\textrm{10}} = 3.22 \times 10^{17}$), indicating that regulation strategies reduced subjective arousal and physiological responding.
For detailed information on post-hoc tests, please see tables \@ref(tab:SupplEffectArousalReg) to \@ref(tab:SupplEffectLevReg) and figures \@ref(fig:SupplFigArousalReg) to \@ref(fig:SupplFigLevReg) in the [supplementary material](#SupplementEffectER). 


#### Subjective effort of ER strategies

To investigate whether ER strategies require cognitive effort, we conducted an rmANOVA comparing the subjective effort ratings of four strategies (active viewing, distraction, distancing, suppression).
We found a significant effect of strategy ($F(2.92, 347.65) = 128.47$, $p < .001$, $\hat{\eta}^2_G = .327$, 90\% CI $[.261, .384]$, $\mathrm{BF}_{\textrm{10}} = 1.84 \times 10^{37}$; see figure\ \@ref(fig:FigSubjEffort)).
Post-hoc test showed significantly higher subjective effort for distraction ($t(357) = -17.92$, $p_\mathrm{\scriptsize Tukey(4)} < .001$, $\mathrm{BF}_{\textrm{10}} = 3.61 \times 10^{30}$), distancing ($t(357) = -15.82$, $p_\mathrm{\scriptsize Tukey(4)} < .001$, $\mathrm{BF}_{\textrm{10}} = 1.60 \times 10^{28}$), and suppression ($t(357) = -12.26$, $p_\mathrm{\scriptsize Tukey(4)} < .001$, $\mathrm{BF}_{\textrm{10}} = 1.27 \times 10^{19}$) compared to active viewing. 
Moreover, we found significantly lower effort during suppression compared with distraction ($t(357) = 5.66$, $p_\mathrm{\scriptsize Tukey(4)} < .001$, $\mathrm{BF}_{\textrm{10}} = 1.61 \times 10^{6}$) and distancing ($t(357) = 3.55$, $p_\mathrm{\scriptsize Tukey(4)} = .002$, $\mathrm{BF}_{\textrm{10}} = 29.19$).

[INSERT FIGURE 3 HERE]

\begin{figure}[H]
\includegraphics[width=\textwidth]{figures/FigSubjEffort} \caption{Subjective effort ratings vizalized as boxplots. Dots represent individual effort ratings placed in 150 qantiles.}(\#fig:FigSubjEffort)
\end{figure}

The cognitive effort expended also played the most important role in the subsequent choice decision, which resembled previous findings of our group[@Scheffel2021]. 
Here, 45.40% stated that they chose the strategy that was easiest for them to implement.
24.40% stated they chose the strategy that was most effective and 11.80% stated their chosen strategy was the easiest and most effective.
A more detailed list of all reasons can be found in Table XX in [supplementary material](#SupplementReasonChoice).

#### Subjective values of ER strategies

Individual SVs could be determined for 120 participants for all three ER strategies.
SVs ranged between 0.005 and 1.00.
In sum, $n=$ 119 had one SV of 1.0, indicating a clear preference for one ER strategy.
Absolute preferences for ER strategies were relatively equally distributed.
Highest SV for distraction was reported by $n=$ 41, for distancing by $n=$ 36, and for suppression by $n=$ 43.

To investigate, which variables can predict individual SVs of ER strategies, a multilevel model approach was chosen.
The ICC of the null model was $ICC=$ 0.19, indicating that the level-2 predictor subject accounted for 19.10% of total variance.
The preregistered model showed a correlation of $r=$ 0.95 of the random effects subjects and recoded strategy ($BF10$ of the variable strategy: $\mathrm{BF}_{\textrm{10}} = \infty$).
Our model explained 0.90% of variance and thus we assumed our model was overfitted due to including recoded strategy as the random slope.
We therefore set a new model without the recoded strategy as the random slope factor to estimate the influence of predictors on SVs more precisely.
The second model followed the specification: 
$$
\begin{split}
SV \sim \text{effort rating} + \text{arousal rating} + \text{utility rating} + corrugator \text{ activity} \\\ + levator \text{ activity} + (1 |subject)
\end{split}
$$ 

The second model explained 0.41% of variance. 
All results of the second model are in Table\ \@ref(tab:TabMLMH5).

[INSERT TABLE 1 HERE]


\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:TabMLMH5}Results of multilevel model predicting subjective values of ER strategies.}

\begin{tabular}{llllll}
\toprule
Parameter & \multicolumn{1}{c}{Beta} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$p$-value} & \multicolumn{1}{c}{$f^{2}$} & \multicolumn{1}{c}{Random Effects (SD)}\\
\midrule
Intercept & $8.03 \times 10^{-1}$ & 0.01 & 0.00 &  & 0.11\\
Effort & $-6.85 \times 10^{-4}$ & 0.00 & 0.00 & 0.03 & \\
Arousal & $-7.84 \times 10^{-5}$ & 0.00 & 0.32 & 0.00 & \\
Utility & $1.42 \times 10^{-3}$ & 0.00 & 0.00 & 0.15 & \\
Corrugator activity & $7.45 \times 10^{-3}$ & 0.00 & 0.04 & 0.00 & \\
Levator activity & $5.32 \times 10^{-3}$ & 0.00 & 0.07 & 0.00 & \\
\bottomrule
\end{tabular}

\end{threeparttable}
\end{center}

\end{table}

The predictors effort rating ($\hat{\beta} = 0.00$, 95\% CI $[0.00, 0.00]$, $t(5,618.96) = -13.98$, $p < .001$), utility rating ($\hat{\beta} = 0.00$, 95\% CI $[0.00, 0.00]$, $t(5,618.96) = 29.49$, $p < .001$), and *Corrugator* activity ($\hat{\beta} = 0.01$, 95\% CI $[0.00, 0.01]$, $t(5,618.96) = 2.09$, $p = .037$) showed a significant association with SVs.
The values were relatively small, so the respective effect size $f^{2}$ was calculated as the explained variance.
Interestingly, utility rating showed the greatest effect size of all predictors ($f^{2}=$ 0.155), indicating that utility rating explained 15.5% of variance in SVs.<!--JZ: Mir wurde mal die Verwendung von Worten wie "interestingly" im Ergebnisteil angekreidet, also die Bewertung vielleicht bis zum Diskussionsteil aufheben-->
Effort rating showed an effect size of $f^{2}=$ 0.035.
The effect sizes of all other predictors were negligibly small ($f^{2}< 0.01$).

#### Associations between subjective values and flexible ER

To investigate the ecological validity of the subjective values of ER strategies we calculated, we tested whether SVs were associated with the actual choice of participants in the choice block.
Therefore, a $\chi^{2}$ test with predicted choice (i.e., the strategy with the highest SV of each participant) and actual choice was computed.
There was a significant association between predicted choice and actual choice ($\chi^2(4, n = 119) = 115.40$, $p < .001$, $\mathrm{BF}_{\textrm{10}} = 1.62 \times 10^{21}$; see figure\ \@ref(fig:FigSVChoice)). <!--JZ: Vielleicht wäre hier eine Heatmap auch ganz nice, das scheint wohl eine gute Visualisierung für einen Chi Square Test zu sein (https://www.analyticsvidhya.com/blog/2021/06/decoding-the-chi-square-test%E2%80%8A-%E2%80%8Ause-along-with-implementation-and-visualization/)-->

[INSERT FIGURE 4 HERE]

\begin{figure}[H]
\includegraphics[width=\textwidth]{figures/FigSVChoice} \caption{Individual subjective values per ER strategy, grouped by choice in last experimental block. Each dot indicates SV of one particpant, the colours indicate their choice in last experimental block. $N=120$}(\#fig:FigSVChoice)
\end{figure}

We then conducted an ordinal regression with the dependent variable "choice" and the individual SVs of all three strategies as independent variables.
Overall model fit was fair with $R^{2}=$ 0.27.
The predictor SV of strategy distraction was found to contribute to the model ($b = -6.29$, 95\% CI $[-10.81, -3.02]$, $z = -3.21$, $p = .001$, $BF10=$ 2.00).
The estimated odds ratio indicated a higher chance of choosing strategy distraction, when SV of that strategy is higher.
Additionally, the predictor SV of strategy suppression was found to contribute to the model ($b = 2.70$, 95\% CI $[0.83, 4.84]$, $z = 2.67$, $p = .008$, $BF10=$ 1.99).
The estimated odds ration indicated that a participant is more likely to later choose suppression, when SV of strategy suppression is higher.

Last, we investigated whether SVs are associated with ER flexibility.
We conducted a logistic regression to inspect whether participants' individual $slopes$ and $intercepts$ of ordered SVs could predict their ER flexibility score.
We found neither a significant association between $slopes$ of SVs and FlexER score ($b = -0.36$, 95\% CI $[-1.28, 0.56]$, $t(117) = -0.77$, $p = .444$, $\mathrm{BF}_{\textrm{10}} = 0.72$), nor between $intercepts$ and FlexER score ($b = 1.32$, 95\% CI $[-1.38, 4.02]$, $t(117) = 0.97$, $p = .336$, $\mathrm{BF}_{\textrm{10}} = 0.85$).
However, model fit was relatively low ($R^2 = .03$, $F(2, 117) = 1.93$, $p = .150$).

## 3.3. Exploratory analyses

We exploratorily wanted to investigate the influence of self-control and the investment trait Need for Cognition (NFC) on individual SVs of ER strategies.
The starting point for this was the model reported before. 
Only predictors that had previously shown a significant association with SVs were included in the model together with level-2 predictors self-control and NFC.
The third model followed the specification:
$$
\begin{split}
SV \sim \text{effort rating} + \text{utility rating} + corrugator \text{ activity} \\\ \text{self-control} + \text{NFC} + (1 |subject)
\end{split}
$$
As one would expect, the predictors effort rating ($\hat{\beta} = 0.00$, 95\% CI $[0.00, 0.00]$, $t(5,620.93) = -14.26$, $p < .001$), utility rating ($\hat{\beta} = 0.00$, 95\% CI $[0.00, 0.00]$, $t(5,620.93) = 33.28$, $p < .001$), and *Corrugator* activity ($\hat{\beta} = 0.01$, 95\% CI $[0.00, 0.01]$, $t(5,620.93) = 2.12$, $p = .034$) showed a significant association with SVs.
In addition, a positive association was also found between self-control and SVs ($\hat{\beta} = 0.02$, 95\% CI $[0.00, 0.05]$, $t(97.97) = 2.04$, $p = .044$).<!--JZ: Auch hier gern die Richtung des Effekts mit hinschreiben (dass Corrugator und Utility beide mit höheren SVs zusammenhängen, ist ja eher unerwartet-->
However, the effect size of self-control was negligibly small ($f^{2}=$ 0.002).
Detailed information can be found in the [supplementary material](#SupplementExploratory).











# Discussion

The present Registered Report sought to evaluate whether our new Cognitive and Affective Discounting (CAD) paradigm is suitable for determining individual subjective values of the ER strategies strategies distraction, distancing, and suppression.
We therefore adapted the Cognitive Effort Discounting Paradigm by Westbrook et al. [-@Westbrook2013] in a way that allows to determine SVs for tasks that have no objective order of difficulty levels. 
The new paradigm was tested on an *n*-back task [@ZernaScheffel2022] and a classic ER paradigm.
The latter was completed by $N=120$ participants. 
As expected, use of ER strategies was associated with decreased subjective and physiological arousal.
This finding is in line with previous meta-analytic findings, indicating the effectiveness of ER strategies, both on subjective as well as physiological levels [@Webb2012;@Zaehringer2020].
Further, we found higher levels of subjective cognitive effort for all ER strategies compared to active viewing. 
This allows us to replicate previous findings from our research group and show that the use of strategies is associated with cognitive effort [@Scheffel2021].
Both measures also showed great variability between individuals.
Taken together, this means that the ER strategies had an effect on the participants as intended: Individuals were able to reduce subjective and physiological responding effectively at the expense of cognitive effort.
We assume that there was a good basis on which individual SVs of ER strategies could be determined.
All in all, evidence was in favour of hypotheses H1 to H5.

Almost all participants showed an absolute preference for one strategy, indicated by an SV of 1. 
We also found a wide range of SVs (between 0.005 and 1.00), suggesting that individuals prefer strategies to different extents.
There was a significant relationship between SVs and choice of strategy. 
Overly frequent the strategy would be chosen by the persons for whom the highest subjective value had been determined before, which speaks in favour of hypothesis H7.
Further, we found associations between individual SVs and different predictors.
Subjective effort, utility, and *Corrugator* muscle activity significantly predicted individual SVs.
Contrary to our hypothesis H6, utility was the best predictor for individual SVs, explaining 15.5 percent of variance in SVs.
However, individual SVs did not show associations with ER flexibility, we therefore found no evidence for hypothesis H7.

## Ecological validity of subjective values of ER strategies

Our goal was to calculate individual subjective values to develop a better understanding of ER stratagem selection.
Most individuals show great variability in the choice of strategies, both, within-strategy and between-strategy[@Blanke2020;@Burr2020;@Elkjaer2022]. 
Greater variability might even adaptive [@Blanke2020;@Aldao2015].
In addition, a wide variety of factors that influence the choice of stratgies in specific situations were examined[@Scheffel2021;@Sheppes2011;@Sheppes2014;@Wilms2020;@Young2020].
Thus, different factors have only rarely been studied together[@Young2020].
Moreover, the usual paradigms used in ER choice research (e.g., Sheppes et al.[@Sheppes2011]) cannot be used to determine what internal subjective value the subjects associated with the strategies.
However, we succeeded in this with our new CAD paradigm.
On the one hand, we were able to show which factors influence the values, but on the other hand, we were able to show the actual practical relevance of the values.
The highest SVs of the individuals were associated with the choice made by the participants. 
Until now, it has been difficult to transfer such findings from the laboratory to everyday life[@Wilms2020].
This could be due to the fact that the strategies that have to be chosen between are often fixed in laboratory tests by the experimental design[@Sheppes2011;@Sheppes2014;@Scheffel2021].
It was therefore attempted to investigate ER choice and influencing factors in everyday life.
However, even there, certain strategies were often prescribed (for example studies, see English et al.[@English2017], Millgram et al.[@Millgram2019], Wilms et al.[@Wilms2020]). 
Although these covered a large area of the emotion-genesis process[@Gross1998emerging], they were nevertheless ultimately fixed.
Of course, the calculation of SVs in our new CAD paradigm is tied to the strategies with which the strategy of interest is compared.
However, it would be possible to use ecological momentary assessment to capture ER strategies[@Koval2020].
This would allow all strategies of the ER repertoire to be recorded for each individual[@Aldao2015]. 
Also those that are rarely used or even marked as maladaptive, such as alcohol consumption or rumination[@Pena-Sarrionandia2015].




Dynamic processes in emotion regulation choice
Jonathan W. Murphy
& Michael A. Young


## Trait character of SVs
Hat das Trait-Charakter?

State character of goals @Wilms2020

## Limitations

Our findings must be considered in light of several limitations.
First, it must be mentioned that a block design was used.
This allows for habituation effects of EMG activity within the block.
However, block designs are common in ER research [@Barreiros2019] and were used in previous studies [@Scheffel2019]. 
Second, it has to be mentioned that subjective arousal, effort, and utility ratings were conducted retrospectively at the end of each block.
It is also known that affect labeling might attenuate emotional experience [@Lieberman2007;@Torre2018]. 
That is why we decided not to have the ratings done after every image.
Furthermore, we were able to confirm our manipulation checks, indicating that implementation of ER strategies was successful, both on subjective and physiological levels.
Taken together, these two facts may have led to slightly lower associations between SVs and predictors.

Third, it is a major limitation that participants had to use three given ER strategies.
It could be that some of the participants did not implement or were used to any of the three strategies in everyday life.
So it may be that none of the strategies has a really high subjective value for the person.
However, strategies for attentional deployment, cognitive change, and response modulation were chosen that meta-analytically proved to be most effective [@Webb2012]. 
Related to that, individual SVs of each person have to be interpreted with caution. 
They depend on the specific context: The stimulus material presented and the strategies that are compared with each other.
Thus, it could be that SVs for one ER strategy would be higher or lower when using other stimuli or valences of stimuli and other comparison strategies.
That is because the computation of SVs is inseparable form the other SVs.

Fourth, the highest value during the discounting paradigm was set to 2 € as fixed value.
Participants should imagine that this was the amount of money they would get when they would repeat this strategy.
Thus, 2 € as an incentive to repeat an entire regulation block could be quite low.
However, we chose this amount because, first, we have followed the original paradigm of Westbrook[@Westbrook2013].
Further it was shown that at least in cognitive effort discounting, a lower incentive could even increase sensitivity in participants for differences in effort[@Bialaszek2017].
n the future, however, it should be examined how the level of incentives affects subjective values.

## Conclusion

# References

```{=tex}
\begingroup
\setlength{\parindent}{-0.5in}
\setlength{\leftskip}{0.5in}
```
::: {#refs custom-style="Bibliography"}
:::

```{=tex}
\endgroup
```
\newpage

# Acknowledgements

This research is partly funded by the German Research Foundation (DFG) as part of the Collaborative Research Center (CRC) 940, and partly funded by centralized funds of the Faculty of Psychology at Technische Universität Dresden.
The funders had no role in study design, data collection and analysis, decision to publish or preparation of the manuscript.
The authors would like to thank Juliana Krause and Maja Hentschel for their help with data collection.

# Competing Interests

The authors declare no competing interests.

```{=tex}
\newpage
\setcounter{figure}{0}
```










# Figures and figure captions


\begin{figure}
\includegraphics[width=\textwidth]{figures/Paradigm_Scheme_T2} \caption{ }(\#fig:ResponsePatternsAppendix)
\end{figure}

*Figure 1.* Exemplary visualization of two response patterns.
In the top half, the person has a clear preference for one of the three strategies.
In the lower half, they have no clear preference and therefore show an inconsistent response pattern.
This pattern can also be represented by our paradigm.

\begin{figure}[H]
\includegraphics[width=\textwidth]{figures/Design_ER-ED} \caption{ }(\#fig:DesignEREDappendix)
\end{figure}

*Figure 2.* Block design of the paradigm.
Every participant starts with two "active viewing" blocks containing neutral (Block 1) and negative (Block 2) pictures.
Order of the regulation blocks (Blocks 3, 4, and 5) is randomized between participants.
After, the discounting procedure takes place.
All three regulation strategies are pairwise compared.
Before the last block, participants can decide which regulation strategy they want to reapply.
Subjective arousal and effort ratings are assessed after each block using a slider on screen with a continuous scale.

# Design Table {#DesignTable}

\includepdf[pages={-}, landscape=true]{Supplement/Design_Table_T2.pdf}

\newpage











# Supplementary Material {#SupplementaryMaterial}

\includepdf[pages={-}, landscape=true]{Supplement/StimList_Suppl.pdf}
\counterwithin{figure}{section}
\counterwithin{table}{section}
\setcounter{section}{19}
\setcounter{figure}{0}
\setcounter{table}{1}
\newpage

## Detailed information on psychometric measures {#SupplementQuestionnaires}

*WHO-5.* General psychological well-being is assessed using the WHO-5 scale[@Bech2004; @Braehler2007].
5 Items such as "Over the past 2 weeks I have felt calm and relaxed." are rated on a 6-point Likert scale raning from 0 (at no time) to 5 (all of the time).
The german version of the scale showed a high internal consistency (Cronbach's $\alpha=.92$)[@Braehler2007].

*Connor-Davidson Resilience Scale.* Resilience is assessed using the Connor-Davidson Resilience Scale (CD-RISC)[@Connor2003; @Campbell-Sills2007; @Sarubin2015].
10 items such as "I am able to adapt to change." are rated on a scale from 0 (not true at all) to 4 (true nearly all the time).
The 10-item version showed a high internal consistency (Cronbach's $\alpha=.84$) and a satisfactory retest-reliability of $r_{tt}=.81$ across 6 month[@Sarubin2015].

*Emotion Regulation Questionnaire.* Habitual use of reappraisal and suppression is measured using the 10-item Emotion Regulation Questionnaire (ERQ)[@GrossJohn2003; @Abler2009].
The scale has items such as "I keep my emotions to myself" (ERQ-suppression - 4 items) and "When I'm faced with a stressful situation, I make myself think about it in a way that helps me stay calm" (ERQ-reappraisal - 6 items), which are answered on a 7-point Likert scale ranging from 1 (strongly disagree) to 7 (strongly agree), and has acceptable to high internal consistency (Cronbach's $\alpha>.75$) [@Preece2020].

*FlexER Scale.* Flexible use of ER strategies is assessed using the FlexER Scale [@Doerfel2019] with items such as "If I want to feel less negative emotions, I have several strategies to achieve this.", which are answered on a 4-point scale ranging from "strongly agree" to "strongly disagree".
Psychometric properties are currently under investigation.

*Implicit Theories Questionnaire.* Implicit theories of willpower in emotional control are assessed using the Implicit Theories Questionnaire of @Bernecker2017.
4 items such as "Having to control a strong emotion makes you exhausted and you are less able to manage your feelings right afterwards." are rated on a 6-point scale ranging from 1 (fully agree) to 6 (do not agree at all).
The questionnaire showed an internal consistency of Cronbach's $\alpha=.87$[@Bernecker2017].

*Need for Cognition Scale.* Need for Cognition (NFC) is assessed with the 16-item short version of the German NFC scale [@Bless1994]. Responses to each item (e.g., "Thinking is not my idea of fun", recoded) are recorded on a 7-point Likert scale ranging from -3 (completely disagree) to +3 (completely agree) and are summed to the total NFC score. The scale shows comparably high internal consistency (Cronbach's $\alpha>.80$)[@Bless1994; @Fleischhauer2010] and a retest reliability of $r_{tt}=.83$ across 8 to 18 weeks [@Fleischhauer2015].

*Self-Regulation Scale.* As one measure of self-control, the Self-Regulation Scale (SRS)[@Schwarzer1999] is used. The scale has 10 items (e.g., "It is difficult for me to suppress thoughts that interfere with what I need to do.", recoded) on a 4-point scale ranging from 1 (not at all true) to 4 (exactly true). It has high internal consistency [Cronbach's $\alpha>.80$; @Schwarzer1999].

*Brief Self-Control Scale.* As a second measure of self-control, the Brief Self-Control Scale (BSCS)[@Tangney2004; @Sproesser2011] is used.
It comprises 13 items (e.g., "I am good at resisting temptations") with a 5-point rating scale ranging from 1 (not at all like me) to 5 (very much like me).
The scale shows acceptable internal consistency (Cronbach's $\alpha=.81$)[@Sproesser2011] .

*Barratt Impulsiveness Scale.* As a third measure of self-control, the Barratt Impulsiveness Scale (BIS-11)[@Patton1995; @Hartmann2011] is used.
Responses to each item (e.g., "I am self-controlled.", recoded) are assessed on a 4-point scale ranging from 1 (never/rarely) to 4 (almost always/always).
An internal consistency of Cronbach's $\alpha=.74$ and a retest reliability of $r_{tt}=.56$ for General Impulsiveness and $r_{tt}=.66$ for Total Score across 6 month were reported [@Hartmann2011].

*Attentional Control Scale.* Attentional control is measured using the Attentional Control Scale (ACS)[@Derryberry2002] with items such as "My concentration is good even if there is music in the room around me".
The 20 items are rated on a 4-point scale ranging from 1 (almost never) to 4 (always).
An internal consistency of Cronbach's $\alpha=.88$ was reported [@Derryberry2002].

\newpage

## Test for normal distribution of predictor variables {#SupplementNV}


\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:TabNV}Results of Shapiro-Wilk test for normal distribution of subjective arousal and effort ratings for all strategies.}

\begin{tabular}{lllll}
\toprule
 & \multicolumn{1}{c}{$M$} & \multicolumn{1}{c}{$SD$} & \multicolumn{1}{c}{$W$} & \multicolumn{1}{c}{$p$}\\
\midrule
Arousal View Neu & 26.63 & 39.12 & 0.68 & 0.00\\
Arousal View Neg & 187.78 & 87.31 & 0.98 & 0.06\\
Arousal Distraction & 158.13 & 92.49 & 0.97 & 0.01\\
Arousal Distancing & 168.62 & 95.75 & 0.98 & 0.04\\
Arousal Suppression & 163.96 & 87.17 & 0.98 & 0.07\\
Effort View Neu & 18.15 & 27.37 & 0.65 & 0.00\\
Effort View Neg & 49.40 & 62.26 & 0.74 & 0.00\\
Effort Distraction & 208.46 & 96.15 & 0.98 & 0.13\\
Effort Distancing & 158.26 & 99.50 & 0.97 & 0.01\\
Effort Suppression & 189.80 & 92.34 & 0.98 & 0.12\\
\bottomrule
\end{tabular}

\end{threeparttable}
\end{center}

\end{table}





\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:TabNV}Results of Shapiro-Wilk test for normal distribution of Corrugator and Levator activity for all strategies.}

\begin{tabular}{lllll}
\toprule
 & \multicolumn{1}{c}{$M$} & \multicolumn{1}{c}{$SD$} & \multicolumn{1}{c}{$W$} & \multicolumn{1}{c}{$p$}\\
\midrule
Corrgator View Neu & 0.04 & 6.99 & 0.05 & 0.00\\
Corrgator View Neg & 1.03 & 7.21 & 0.19 & 0.00\\
Corrgator Distraction & 0.00 & 7.67 & 0.04 & 0.00\\
Corrgator Distancing & 0.07 & 3.78 & 0.08 & 0.00\\
Corrgator Suppression & 0.25 & 1.92 & 0.35 & 0.00\\
Levator View Neu & 0.09 & 1.84 & 0.38 & 0.00\\
Levator View Neg & 0.58 & 3.20 & 0.43 & 0.00\\
Levator Distraction & -0.05 & 1.16 & 0.52 & 0.00\\
Levator Distancing & -0.03 & 0.92 & 0.48 & 0.00\\
Levator Suppression & 0.01 & 1.00 & 0.55 & 0.00\\
\bottomrule
\end{tabular}

\end{threeparttable}
\end{center}

\end{table}

\newpage

## Post-hoc tests of strategies for effects of ER on subjective arousal and physiological responding {#SupplementEffectER} 


\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:SupplEffectArousalReg}Post-hoc tests for effects of ER strategies on subjective arousal ratings.}

\footnotesize{

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{neg} - Distraction$ & 29.65 & 6.68 & 357.00 & 4.44 & 0.00 & 168.48 & 0.05 & {}[0.02, 1.00]\\
$View_{neg} - Distancing$ & 23.82 & 6.68 & 357.00 & 3.57 & 0.00 & 62.99 & 0.03 & {}[0.01, 1.00]\\
$View_{neg} - Suppression$ & 19.16 & 6.68 & 357.00 & 2.87 & 0.03 & 1.97 & 0.02 & {}[0.00, 1.00]\\
$Distraction - Distancing$ & -5.83 & 6.68 & 357.00 & -0.87 & 1.00 & 0.18 & 2.13e-03 & {}[0.00, 1.00]\\
$Distraction - Suppression$ & -10.49 & 6.68 & 357.00 & -1.57 & 0.70 & 0.31 & 6.86e-03 & {}[0.00, 1.00]\\
$Distancing - Suppression$ & -4.66 & 6.68 & 357.00 & -0.70 & 1.00 & 0.14 & 1.36e-03 & {}[0.00, 1.00]\\
\bottomrule
\end{tabular}

}

\end{threeparttable}
\end{center}

\end{table}

\begin{figure}[H]
\includegraphics[width=\textwidth]{figures/FigSubjArousal} \caption{Subjective arousal ratings vizalized as boxplots. Dots represent individual effort ratings placed in 150 qantiles.}(\#fig:SupplFigArousalReg)
\end{figure}


\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:SupplEffectCorrReg}Post-hoc tests for effects of ER strategies on Corrugator activity}

\footnotesize{

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{neg} - Distraction$ & 0.18 & 0.04 & 351.00 & 4.79 & 0.00 & 21,919.73 & 0.06 & {}[0.03, 1.00]\\
$View_{neg} - Distancing$ & 0.19 & 0.04 & 351.00 & 5.09 & 0.00 & 139,814.01 & 0.07 & {}[0.03, 1.00]\\
$View_{neg} - Suppression$ & 0.21 & 0.04 & 351.00 & 5.67 & 0.00 & $1.84 \times 10^{7}$ & 0.08 & {}[0.04, 1.00]\\
$Distraction - Distancing$ & 0.01 & 0.04 & 351.00 & 0.30 & 1.00 & $3.77 \times 10^{-2}$ & 2.61e-04 & {}[0.00, 1.00]\\
$Distraction - Suppression$ & 0.03 & 0.04 & 351.00 & 0.88 & 1.00 & $8.02 \times 10^{-2}$ & 2.21e-03 & {}[0.00, 1.00]\\
$Distancing - Suppression$ & 0.02 & 0.04 & 351.00 & 0.58 & 1.00 & $4.79 \times 10^{-2}$ & 9.51e-04 & {}[0.00, 1.00]\\
\bottomrule
\end{tabular}

}

\end{threeparttable}
\end{center}

\end{table}

\begin{figure}[H]
\includegraphics[width=\textwidth]{figures/FigCorrReg} \caption{Corrugator activity in mV vizalized as boxplots. Dots represent individual Levatorr activity measures placed in 150 qantiles.}(\#fig:SupplFigCorrReg)
\end{figure}


\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:SupplEffectLevReg}Post-hoc tests for effects of ER strategies on Levator activity}

\footnotesize{

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{neg} - Distraction$ & 0.34 & 0.05 & 351.00 & 6.73 & 0.00 & $2.02 \times 10^{11}$ & 0.11 & {}[0.07, 1.00]\\
$View_{neg} - Distancing$ & 0.28 & 0.05 & 351.00 & 5.66 & 0.00 & $3.99 \times 10^{7}$ & 0.08 & {}[0.04, 1.00]\\
$View_{neg} - Suppression$ & 0.32 & 0.05 & 351.00 & 6.37 & 0.00 & $8.60 \times 10^{10}$ & 0.10 & {}[0.06, 1.00]\\
$Distraction - Distancing$ & -0.05 & 0.05 & 351.00 & -1.07 & 1.00 & 0.22 & 3.26e-03 & {}[0.00, 1.00]\\
$Distraction - Suppression$ & -0.02 & 0.05 & 351.00 & -0.36 & 1.00 & $3.91 \times 10^{-2}$ & 3.70e-04 & {}[0.00, 1.00]\\
$Distancing - Suppression$ & 0.04 & 0.05 & 351.00 & 0.71 & 1.00 & $9.86 \times 10^{-2}$ & 1.44e-03 & {}[0.00, 1.00]\\
\bottomrule
\end{tabular}

}

\end{threeparttable}
\end{center}

\end{table}

\begin{figure}[H]
\includegraphics[width=\textwidth]{figures/FigLevReg} \caption{Levator activity in mV vizalized as boxplots. Dots represent individual Levator activity measures placed in 150 qantiles.}(\#fig:SupplFigLevReg)
\end{figure}
\newpage

## Reasons for decision made by the participants in the last regulation block

\newpage

## Exploratory analysis: Association between SVs and self-control and NFC


\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:TabExp}Exploratory analysis: Results of MLM predicting SVs of ER strategies with level 2 predictors self-control and NFC.}

\begin{tabular}{llllll}
\toprule
Parameter & \multicolumn{1}{c}{Beta} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$p$-value} & \multicolumn{1}{c}{$f^{2}$} & \multicolumn{1}{c}{Random Effects (SD)}\\
\midrule
Intercept & $8.03 \times 10^{-1}$ & 0.01 & 0.00 &  & 0.11\\
Effort & $-6.93 \times 10^{-4}$ & 0.00 & 0.00 & 0.04 & \\
Utility & $1.44 \times 10^{-3}$ & 0.00 & 0.00 & 0.20 & \\
Corrugator activity & $7.54 \times 10^{-3}$ & 0.00 & 0.03 & 0.00 & \\
Self-Control & $2.44 \times 10^{-2}$ & 0.01 & 0.04 & 0.00 & \\
NFC & $7.58 \times 10^{-4}$ & 0.00 & 0.44 & 0.00 & \\
\bottomrule
\end{tabular}

\end{threeparttable}
\end{center}

\end{table}
