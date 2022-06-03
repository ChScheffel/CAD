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
wordcount         : "5630"
bibliography      : ER_ED.bib
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

---
\renewcommand\thesection{\Alph{section}}
\counterwithout{figure}{section}
\setcounter{figure}{0}
---












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
In a separate study, we will test our adapted paradigm together with a *n*-back task and explore whether this paradigm can describe individuals that do not prefer the easiest *n*-back option (see Zerna et al.[@Zerna2022]).

\begin{figure}
\includegraphics[width=\textwidth]{C:/Users/scheffel/Scheffel/Forschung/A_Projects/2021_CERED/CAD/06_Paper/ER-ED/figures/Paradigm_Scheme_T2} \caption{Exemplary visualization of two response patterns. In the top half, the person has a clear preference for one of the three strategies. In the lower half, they have no clear preference and therefore show an inconsistent response pattern. This pattern can be represented by our paradigm.}(\#fig:ResponsePatterns)
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
The R Markdown file used to analyze the data and write this document, as well as the raw data and the materials are freely available at https://github.com/ChScheffel/CERED.
A complete list of all measures assessed in the study can be found at OSF (<https://osf.io/vnj8x/>) and GitHub (https://github.com/ChScheffel/CERED).

## 2.1 Ethics information

The study protocol complies with all relevant ethical regulations and was approved by the ethics committee of the Technische Universität Dresden (reference number EK50012022). 
Prior to testing, written informed consent will be obtained.
Participants will receive 30 € in total or course credit for participation.

## 2.2 Pilot data

The newly developed ER paradigm was tested in a pilot study with $N=16$ participants (9 female; age: $M = 24.1\text{ }\pm\text{ }SD = 3.6$).
Regarding self-reported arousal, results showed significant higher subjective arousal for active viewing of negative compared to neutral pictures.
However, ER strategies did not lead to a reduction of subjective arousal compared to active viewing of negative pictures.
Regarding physiological responses, ER strategies were associated with reduced facial muscle activity of the *corrugator* and *levator* compared to active viewing of negative pictures.
In accordance with our previous study[@Scheffel2021], we found that the use of ER strategies compared to active viewing was associated with increased subjective effort.
All results are detailed in the [Supplementary Material](#SupplementaryMaterial)

## 2.3 Design

Young healthy participants (aged 18 to 30 years) will be recruited using the software *ORSEE*[@Greiner2015] at the Technische Universität Dresden.
Participants will be excluded from participation if they do not fluently speak German, have current or a history of psychological disorders or neurological trauma, or report to take medication.
Participants will be invited to complete an online survey containing different questionnaires to assess broad and narrow personality traits and measures of well-being.
The study consists of two lab sessions, which will take place in a shielded cabin with constant lighting.
Before each session, participants will receive information about the respective experimental procedure and provide informed consent.
In the first session participants will fill out a demographic questionnaire and complete an n-back task with the levels one to four.
Then, they will complete an effort discounting (ED) procedure regarding the n-back levels on screen, followed by a random repetition of one n-back level.
The second session will take place exactly one week after session one.
Participants will provide informed consent and receive written instructions on the ER paradigm and ER strategies that they should apply.
A brief training will ensure that all participants are able to implement the ER strategies.
Next, electrodes to measure facial EMG will be attached and the ER paradigm will be conducted, followed by an ED procedure regarding the ER strategies.
After that, participants will choose one ER strategy to repeat one more time.
Study data will be collected and managed using REDCap electronic data capture tools hosted at Technische Universität Dresden[@Harris2009; @Harris2019].

### 2.3.1 Psychometric measures

The online survey will contain a number of questionnaires. 
In the focus of the current project is the Flexible Emotion Regulation Scale (FlexER)[@Doerfel2019].  
It assess flexible use of ER strategies with items such as "If I want to feel less negative emotions, I have several strategies to achieve this.", which we define as ER flexibility. 
The items are rated on a 4-point scale ranging from "strongly agree" to "strongly disagree".

Further psychological constructs will be assessed but have no clear hypothesies in the present work an are therefore investigated only exploratory:
General psychological well-being will be assessed using the German version of the WHO-5 scale[@Bech2004; @Braehler2007].
To measure resilience, the German version 10-item-form of the Connor-Davidson resilience Scale (CD-RISC)[@Connor2003,@Campbell-Sills2007; @Sarubin2015] will be used.
Habitual use of ER will be assessed using the German version of the Emotion Regulation Questionnaire (ERQ)[@GrossJohn2003; @Abler2009].
Implicit theories of willpower in emotion control will be assessed using the implicit theories questionnaire from Bernecker and Job[@Bernecker2017].
To assess Need for Cognition, the German version short form of the Need for Cognition Scale[@Cacioppo1982; @Bless1994] will be used.
To assess self-control [@Paschke2016], sum scores of the German versions of the following questionnaires will be used: the Self-Regulation Scale (SRS)[@Schwarzer1999], the Brief Self-Control Scale (BSCS)[@Tangney2004; @Sproesser2011], and the Barratt Impulsiveness Scale (BIS-11)[@Patton1995; @Hartmann2011].
Attentional control will be assessed using the Attentional Control Scale (ACS)[@Derryberry2002].
For more detailed information on psychometric properties of the questionnaires, please see [supplementary material](#SupplementQuestionnaires). 

### 2.3.2 Emotion regulation paradigm

The ER paradigm will consist of three parts that will be described in the following.

*Part one: ER task.* <br> Part one will be a standard ER task in a block design (see Figure \@ref(fig:DesignERED)), similar to paradigms previously used by our group[@Scheffel2021].
Participants will be told to actively view neutral and negative pictures (see [2.3.3](##stimuli)) or to regulate all upcoming emotions by means of distraction, distancing, and expressive suppression, respectively.
Every participant first will have the condition "active viewing-neutral" that serves as a baseline condition.
During this block, 20 neutral pictures will be presented.
Participants will be asked to "actively view all pictures and permit all emotions that may arise." 
In the second block, participants will actively view negative pictures.
During the third, fourth, and fifth block, participants will see negative pictures and will be asked to regulate their emotions using distraction, distancing, and suppression.
In order to achieve distraction, participants will be asked to think of a geometric object or an everyday activity, like brushing their teeth.
During distancing, participants will be asked to "take the position of a non-involved observer, thinking about the picture in a neutral way." 
Participants will be told not to re-interpret the situation or attaching a different meaning to the situation.
During suppression, participants will be told to "suppress their emotional facial expression." 
They should imagine being observed by a third person that should not be able to tell by looking at the facial expression whether the person is looking at an emotional picture.
Participants will be instructed not to suppress their thoughts or change their facial expression to the opposite[@Scheffel2021].
All participants will receive written instruction and complete a training session.
After the training session, participants will be asked about their applied ER strategies to avoid misapplication.
The order of the three regulation blocks (distraction, distancing, and suppression) will be randomized between participants.
Each of the blocks consisted of 20 trials showing neutral (Block 1) and negative (Blocks 2, 3, 4, 5) pictures.
Each trial began with a fixation cross that lasted 3 to 5 seconds (random uniform distributed).
It was followed by neutral or negative picture for a total of 6 seconds.
After each block, participants retrospectively rated their subjective emotional arousal ("not at all aroused" to "very highly aroused"), their subjective effort ("not very exhausting" to "very exhausting"), and - after the ragulation blocks - the utility of the respective strategy ("not useful at all" to "very useful") on a continuous scale using a slider on screen.

*Part two: ER effort discounting.* <br> In the second part, ER effort discounting will take place.
The procedure of the discounting will follow the COG-ED paradigm by Westbrook et al.[-@Westbrook2013] with a major change.
We will use the following adaption that allows the computation of SVs for different strategies without presuming that all individuals would inherently evaluate the same strategy as the easiest one: For each possible pairing (distraction vs. distancing, distraction vs. suppression, and distancing vs. suppression), each of the two strategies will be presented with a monetary reward.
The order of the pairings will be randomized.
Because there is no strategy that is objectively more difficult, we will add an initial comparison that begins with the option "1 € for strategy A or 1 € for strategy B".
The participants decide by clicking the on-screen button of the respective option.
The strategy that is not chosen will be assigned the fixed value of 2 €, the chosen strategy will be assigned a starting value of 1 €.
From this point on, comparisons between strategies will follow the original COG-ED paradigm[@Westbrook2013].
Each pairing is presented six consecutive times, and with each decision the reward of the strategy with the starting value of 1 € is either lowered (if this strategy was chosen) or raised (if the strategy with the fixed 2 € reward was chosen).
The adjustment starts at 0.50 € and each is half the adjustment of the previous step, rounded to two digits after the decimal point.
If a participant always chooses the strategy with the fixed 2 € reward, the other strategy's last value on display will be 1.97 €, if they always choose the lower strategy, its last value will be 0.03 €.
The sixth adjustment of 0.02 € will be done during data analysis, based on the participants' decision in the last display of the pairing.
Participants will be instructed to decide as realistically as possible by imagining that the monetary reward is actually available for choice.

*Part three: ER choice.* <br> After the discounting part, participants will choose which one of the three ER strategies (distraction, distancing or suppression) they want to re-apply.
Importantly, there will be no further instruction on what basis they should make their decision.
Participants should make their decision freely, according to criteria they consider important for themselves.
However, participants will be asked to state the reasons for the decision afterwards.
As soon as they have decided, they will see the respective instruction and the block with another 20 negative pictures starts.

\begin{figure}
\includegraphics[width=\textwidth]{C:/Users/scheffel/Scheffel/Forschung/A_Projects/2021_CERED/CAD/06_Paper/ER-ED/figures/Design_ER-ED} \caption{Block design of the paradigm. Every participant starts with two "active viewing" blocks continaing neutral (Block 1) and negative (Block 2) pictures. Order of the regulation blocks (Blocks 3, 4, and 5) is randomized between participants. After, the discounting procedure takes place. All three regulation strategies are pairwise compared. Before the last block, participants can decide which regulation strategy they want to reapply. Subjective arousal and effort ratings are assessed after each block using a slider on screen with a continuous scale.}(\#fig:DesignERED)
\end{figure}

### 2.3.3 Stimuli

Pictures that will be used in the paradigm are selected from the Emotional Picture Set (EmoPicS) [@Wessa2010] and the International Affective Picture System (IAPS)[@Lang2008].
The 20 neutral pictures (Valence (V): *M* $\pm$ *SD* = 4.81 $\pm$ 0.51; Arousal (A): *M* $\pm$ *SD* = 3 $\pm$ 0.65) depicted content related to the categories persons, objects, and scenes.
Further, 100 negative pictures, featuring categories animals, body, disaster, disgust, injury, suffering, violence, and weapons, will be used.
An evolutionary algorithm [@Yu2010] is used to cluster these pictures into five sets with comparable valence and arousal values (set one: V: *M* $\pm$ *SD* = 2.84 $\pm$ 0.57, A: *M* $\pm$ *SD* = 5.62 $\pm$ 0.34; set two: V: *M* $\pm$ *SD* = 2.64 $\pm$ 0.46, A: *M* $\pm$ *SD* = 5.58 $\pm$ 0.35; set three: V: *M* $\pm$ *SD* = 2.82 $\pm$ 0.62, A: *M* $\pm$ *SD* = 5.60 $\pm$ 0.39; set four: V: *M* $\pm$ *SD* = 2.65 $\pm$ 0.75, A: *M* $\pm$ *SD* = 5.61 $\pm$ 0.41; set five: V: *M* $\pm$ *SD* = 2.74 $\pm$ 0.70, A: *M* $\pm$ *SD* = 5.63 $\pm$ 0.37).
A complete list of all pictures and their classification into sets can be found in supplementary material 1.
The five sets of negative pictures will be assigned randomly to the blocks.

### 2.3.4 Facial electromyography

Bipolar facial electromyography (EMG) will be measured for *corrugator supercilii* and *levator labii* as indices of affective valence[@Bradley2000], similar to previous work by our group[@Gaertner2021].
Two passive surface Ag/AgCl electrodes (8 mm inner diameter, 10 mm distance between electrodes) will be placed over each left muscle according to the guidelines of @Fridlund1986.
The ground electrode will be placed over the left *Mastoid*.
Before electrode placement, the skin will be abraded with Every abrasive paste, cleaned with alcohol, and filled with Lectron III electrolyte gel.
Raw signals will be amplified by a BrainAmp amplifier (Brain Products Inc., Gilching, Germany).
Impedance level will be kept below 10 $k\Omega$. 
Data will be sampled at 1000 Hz, filtered, rectified and integrated. 
A 20 Hz high pass (order 8), a 300 Hz low pass (order 8), and a 50 Hz notch filter will be applied to both signals.
Corrugator and Levator EMG will be analyzed during the 6 s of picture presentation.
EMG data will be baseline-corrected using a time window of 2 s prior to stimulus onset [@Bradley2000]. 
Last, the sampling rate will be changed to 100 Hz, and EMG data will be averaged for each condition and each participant.

## 2.4 Sampling plan

Sample size calculation is done using *G\*Power*[@Faul2007; @Faul2009].
In a meta-analysis of Zaehringer and colleagues[-@Zaehringer2020], effect sizes of ER on peripheral-physiological measures were reported:
To find an effect of $d=-0.32$ of ER on *corrugator* muscle activity with $\alpha=.05$ and $\beta=.95$, data of at least $N=85$ have to be analyzed.
Power analyses of all other hypotheses yielded smaller sample sizes.
However, if participants withdraw from study participation, technical failures occur, or experimenter considers the participant for not suitable for study participation (e.g., because the participant does not follow instructions or shows great fatigue), respective data will also be excluded from further analyses.
Therefore, we aim to collect data of $N=120$ participants, about $50%$ more data sets, than necessary.
Detailed information on power calculation for each hypothesis can be found in the [design table](#DesignTable).

## 2.5 Analysis plan

Data collection and analysis will not be performed blind to the conditions of the experiments.
Data of whole participants will be excluded from analysis if participants withdraw their consent or they state that they did not follow experimental instructions.
EMG data of subjects will be excluded from analysis if errors occured during recording.
No further data exclusions are planned.
The level of significance will be set to $\alpha=.05$.
For hypotheses H1-4, repeated measures analysis of variance (rmANOVA) will be conducted and estimated marginal means will be computed using the *afex* package[@Singmann2021].
Greenhouse-Geisser-corrected degrees of freedom and associated $p$-values and will be reported when the assumption of sphericity is violated.
If the within-subjects factor of interest is significant, pairwise contrasts will be calculated using Bonferroni adjustment for multiple testing.
Proportion of explained variance $\eta_{p}^{2}$ will be reported as a measure of effect size.

*Effect of valence on arousal and facial EMG.*<br> 
To examine the impact of valence of emotional pictures on subjective arousal ratings (H1a), a rmANOVA with the factor valence (neutral and negative) for the strategy active viewing will be conducted.
To examine the impact of valence on physiolocigal responding (H1b and H1c), a rmANOVA with the factor valence (neutral and negative) for the strategy active viewing will be conducted for EMG *corrugator* and *levator* activity.

*Effects of emotion regulation on arousal, facial EMG and effort.* <br> 
To investigate the effects of the three ER strategies on subjective arousal (H2a), another rmANOVA  with the factor strategy (active viewing - negative, distraction, distancing, and suppression) for subjective arousal ratings will be conducted.
To examine the effects of the three ER strategies on physiological responding (H3a and H3b), another rmANOVA with the factor strategy (active viewing - negative, distraction, distancing, and suppression) for EMG *corrugator* and *levator* activity will be conducted.
To examine the effect of ER strategies on subjective effort (H4a), a rmANOVA with the factor strategy (active viewing, distraction, distancing, and suppression) for subjective effort ratings will be conducted.

*Subjective values of emotion regulation strategies.* <br> For each ER strategy, SVs will be calculated as follows: first, the value 0.02 € will be added to or subtracted from the last monetary value of the flexible strategy, depending on the participant's last choice.
Second, the resulting monetary value will be divided by 2.00 € to arrive at the SV of the opposite strategy in each pairing.
Therefore, the SVs of the flexible strategies are 1, because they were chosen in the initial comparison of each pairing in which the same value was offered for both strategies, so they are the preferred strategy of each pairing.
The SVs of the fixed strategies lay between 0 and 1, with lower values indicating that the participant would need a much higher monetary incentive to choose this strategy over the other one in the pairing. 
The final SV per strategy for each participant will be computed by averaging the SVs of each strategy across pairings.

To explore the association between subjective effort (H5a), subjective arousal (H5b), subjective utility (H5c), and physiological responding (H5d,e) on SVs, a multilevel model (MLM) will be specified using the $lmerTest$ package[@Kuznetsova2017].
First, ER strategies will be recoded and centered for each subject according to their individual SVs: The strategy with the highest SV will be coded as -1, the strategy with the second highest SV 0, and the strategy with the lowest SV will be coded as 1.
Restricted maximum likelihood (REML) will be applied to fit the model.
A random slopes model of SVs including subjective effort (effort ratings), subjective arousal (arousal ratings), and physiological responses (*corrugator* and *levator* activity) as level-1-predictors will be specified.
$$
SV \sim strategy\ + \text{effort rating} + \text{arousal rating} + \text{utility} + corrugator \text{ activity} + levator \text{ activity} + (strategy|subject)
$$ 
Level-1-predictors will be centered within cluster[@Enders2007].
Residuals of the final model will be inspected visually.
Intraclass correlation coefficient (ICC), $\rho$, will be reported for each model (null model, as well as full model).

To investigate whether individual SVs predict ER choice (H7a), a Chi-squared test with predicted choice (highest SV of each participant) and actual choice will be computed.
Furthermore, an ordinal logistic regression with the dependent variable choice and independent variables SVs of each strategy will be computed.

The association between flexible ER and SVs of ER strategies (H7b) will be investigated with a linear regression using the individual $intercept$ and $slope$ of each participants' SVs to predict their FlexER score.
To this end, for each participant, SVs will be sorted by magnitude in descending order and entered as dependent variable in a linear model, with strategy (centered, i.e., -1, 0, 1) as independent variable.
The resulting $intercept$ informs about the extent to which an individual considers any or all of the ER strategies as useful for regulation their emotion, while the $slope$ informs about the flexibility in the use of emotion regulation strategies. 
The individual intercepts and slopes will then be entered as predictors in a regression model with the FlexER score as dependent variable. 
A positive association with the predictor $intercept$ would indicate that overall higher SVs attached to ER strategies predicts higher scores on the FlexER scale. 
A positive association with the predictor $slope$ would indicate that less negative slopes, i.e., a smaller preference for a given ER strategy, would be associated with a higher score of the FlexER scale.

The influence of personality traits on SVs will be investigated exploratorily.
Therefore, the MLM specified above will be extended by the level-2-predictors NFC and self-control.

For each result of the analyses, both $p$-values and Bayes factors $BF10$, calculated using the *BayesFactor* package[@Morey2021], will be reported. 
Bayes factors are calculated using the default prior widths of the functions *anovaBF*, *lmBF* and *regressionBF*.

## Data availability

The data of this study can be downloaded from [osf.io/vnj8x/](https://osf.io/vnj8x/).

## Code availability

The paradigm code, as well as the R Markdown file used to analyze the data and write this document is available at our [Github repository](https://github.com/ChScheffel/CERED).

# References

\begingroup
\setlength{\parindent}{-0.5in}
\setlength{\leftskip}{0.5in}

<div id="refs" custom-style="Bibliography"></div>
\endgroup

\newpage

# Acknowledgements

This research is partly funded by the German Research Foundation (DFG) as part of the Collaborative Research Center (CRC) 940.
Additionally, we have applied for funding of the participants' compensation from centralized funds of the Faculty of Psychology at Technische Universität Dresden.
Applications for the centralized funds will be reviewed in May.
Regardless of whether or not this additional funding will be granted, the study can commence immediately.
The funders have/had no role in study design, data collection and analysis, decision to publish or preparation of the manuscript.

# Competing Interests

The authors declare no competing interests.

\newpage
\setcounter{figure}{0}

# Figures and figure captions

\newpage
\begin{figure}
\includegraphics[width=\textwidth]{C:/Users/scheffel/Scheffel/Forschung/A_Projects/2021_CERED/CAD/06_Paper/ER-ED/figures/Paradigm_Scheme_T2} \caption{ }(\#fig:ResponsePatternsAppendix)
\end{figure}
*Figure 1.* 
Exemplary visualization of two response patterns. 
In the top half, the person has a clear preference for one of the three strategies. 
In the lower half, they have no clear preference and therefore show an inconsistent response pattern. 
This pattern can also be represented by our paradigm.

\begin{figure}[H]
\includegraphics[width=\textwidth]{C:/Users/scheffel/Scheffel/Forschung/A_Projects/2021_CERED/CAD/06_Paper/ER-ED/figures/Design_ER-ED} \caption{ }(\#fig:DesignEREDappendix)
\end{figure}
*Figure 2.* 
Block design of the paradigm. 
Every participant starts with two "active viewing" blocks continaing neutral (Block 1) and negative (Block 2) pictures. 
Order of the regulation blocks (Blocks 3, 4, and 5) is randomized between participants. After, the discounting procedure takes place.
All three regulation strategies are pairwise compared. Before the last block, participants can decide which regulation strategy they want to reapply. 
Subjective arousal and effort ratings are assessed after each block using a slider on screen with a continuous scale.

# Design Table {#DesignTable}

\includepdf[pages={-}, landscape=true]{Supplement/Design_Table_T2.pdf}

\newpage

# Supplementary Material {#SupplementaryMaterial}

\includepdf[pages={-}, landscape=true]{Supplement/StimList_Suppl.pdf}

\newpage

## Detailed information on psychometric measures {#SupplementQuestionnaires}

*WHO-5.*
General psychological well-being is assessed using the WHO-5 scale[@Bech2004; @Braehler2007].
5 Items such as "Over the past 2 weeks I have felt calm and relaxed." are rated on a 6-point Likert scale raning from 0 (at no time) to 5 (all of the time).
The german version of the scale showed a high internal consistency (Cronbach's $\alpha=.92$)[@Braehler2007].

*Connor-Davidson Resilience Scale.*
Resilience is assessed using the Connor-Davidson Resilience Scale (CD-RISC)[@Connor2003; @Campbell-Sills2007; @Sarubin2015].
10 items such as "I am able to adapt to change." are rated on a scale from 0 (not true at all) to 4 (true nearly all the time).
The 10-item version showed a high internal consistency (Cronbach's $\alpha=.84$) and a satisfactory retest-reliability of $r_{tt}=.81$ across 6 month[@Sarubin2015].

*Emotion Regulation Questionnaire.* 
Habitual use of reappraisal and suppression is measured using the 10-item Emotion Regulation Questionnaire (ERQ)[@GrossJohn2003;@Abler2009].
The scale has items such as "I keep my emotions to myself" (ERQ-suppression - 4 items) and "When I'm faced with a stressful situation, I make myself think about it in a way that helps me stay calm" (ERQ-reappraisal - 6 items), which are answered on a 7-point Likert scale ranging from 1 (strongly disagree) to 7 (strongly agree), and has acceptable to high internal consistency (Cronbach’s $\alpha>.75$) [@Preece2020].

*FlexER Scale.*
Flexible use of ER strategies is assessed using the FlexER Scale [@Doerfel2019] with items such as "If I want to feel less negative emotions, I have several strategies to achieve this.", which are answered on a 4-point scale ranging from "strongly agree" to "strongly disagree".
Psychometric properties are currently under investigation.

*Implicit Theories Questionnaire.*
Implicit theories of willpower in emotional control are assessed using the Implicit Theories Questionnaire of @Bernecker2017.
4 items such as "Having to control a strong emotion makes you exhausted and you are less able to manage your feelings right afterwards." are rated on a 6-point scale ranging from 1 (fully agree) to 6 (do not agree at all).
The questionnaire showed an internal consistency of Cronbach's $\alpha=.87$[@Bernecker2017].

*Need for Cognition Scale.*
Need for Cognition (NFC) is assessed with the 16-item short version of the German NFC scale [@Bless1994]. 
Responses to each item (e.g., "Thinking is not my idea of fun", recoded) are recorded on a 7-point Likert scale ranging from -3 (completely disagree) to +3 (completely agree) and are summed to the total NFC score. 
The scale shows comparably high internal consistency (Cronbach's $\alpha>.80$)[@Bless1994; @Fleischhauer2010] and a retest reliability of $r_{tt}=.83$ across 8 to 18 weeks [@Fleischhauer2015].

*Self-Regulation Scale.*
As one measure of self-control, the Self-Regulation Scale (SRS)[@Schwarzer1999] is used.
The scale has 10 items (e.g., "It is difficult for me to suppress thoughts that interfere with what I need to do.", recoded) on a 4-point scale ranging from 1 (not at all true) to 4 (exactly true).
It has high internal consistency [Cronbach's $\alpha>.80$; @Schwarzer1999].

*Brief Self-Control Scale.* 
As a second measure of self-control, the Brief Self-Control Scale (BSCS)[@Tangney2004; @Sproesser2011] is used. 
It comprises 13 items (e.g., “I am good at resisting temptations”) with a 5-point rating scale ranging from 1 (not at all like me) to 5 (very much like me). 
The scale shows acceptable internal consistency (Cronbach’s $\alpha=.81$)[@Sproesser2011] .

*Barratt Impulsiveness Scale.*
As a third measure of self-control, the Barratt Impulsiveness Scale (BIS-11)[@Patton1995; @Hartmann2011] is used.
Responses to each item (e.g., "I am self-controlled.", recoded) are assessed on a 4-point scale ranging from 1 (never/rarely) to 4 (almost always/always).
An internal consistency of Cronbach's $\alpha=.74$ and a retest reliability of $r_{tt}=.56$ for General Impulsiveness and $r_{tt}=.66$ for Total Score across 6 month were reported [@Hartmann2011].

*Attentional Control Scale.*
Attentional control is measured using the Attentional Control Scale (ACS)[@Derryberry2002] with items such as "My concentration is good even if there is music in the room around me".
The 20 items are rated on a 4-point scale ranging from 1 (almost never) to 4 (always).
An internal consistency of Cronbach's $\alpha=.88$ was reported [@Derryberry2002].


\newpage
## Pilot study: Subjective arousal in the conditions "Active viewing - neutral" and "Active viewing - negative"
ANOVA:


\begin{tabular}{l|l|l|l|l|l}
\hline
Effect & df & MSE & F & ges & p.value\\
\hline
block & 1, 15 & 3895.91 & 34.32 *** & .475 & <.001\\
\hline
\end{tabular}

 
$BF10=$ 1,244.99

Paired contrasts:

\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:unnamed-chunk-3}Paired contrasts for the rmANOVA comparing subjective arousal of negative and neutral pictures in the condition "active viewing".}

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{neutral} - View_{negative}$ & -129.28 & 22.07 & 15.00 & -5.86 & 0.00 & 794.78 & 0.70 & {}[0.43, 1.00]\\
\bottomrule
\addlinespace
\end{tabular}

\begin{tablenotes}[para]
\normalsize{\textit{Note.} $SE$ = standard error, $df$ = degrees of freedom, $t$ = $t$-statistic, $p$ = $p$-value, CI = confidence interval.}
\end{tablenotes}

\end{threeparttable}
\end{center}

\end{table}
Figure:
\begin{figure}[H]
\includegraphics[width=0.75\linewidth]{Manuscript_ERED_Stage1_files/figure-latex/FigSubjArousalViewPilot-1} \caption{Subjective arousal ratings for the conditions "Active viewing - neutral" and "Active viewing - negative" visualized as boxplots. Each dot represents the effort rating of a single subject. Bold dots represent outliers.}(\#fig:FigSubjArousalViewPilot)
\end{figure}
## Pilot study: Subjective arousal in the conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression"
ANOVA:

\begin{tabular}{l|l|l|l|l|l}
\hline
Effect & df & MSE & F & ges & p.value\\
\hline
block & 2.79, 41.89 & 2238.27 & 1.17 & .011 & .332\\
\hline
\end{tabular}


$BF10=$ 0.11

Paired contrasts:

\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:unnamed-chunk-4}Paired contrasts for the rmANOVA comparing subjective arousal of conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression".}

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{negative} - Distraction$ & -0.74 & 16.14 & 45.00 & -0.05 & 1.00 & 0.26 & 4.68e-05 & {}[0.00, 1.00]\\
$View_{negative} - Distancing$ & -5.35 & 16.14 & 45.00 & -0.33 & 1.00 & 0.27 & 2.43e-03 & {}[0.00, 1.00]\\
$View_{negative} - Suppression$ & -26.23 & 16.14 & 45.00 & -1.63 & 0.67 & 1.25 & 0.06 & {}[0.00, 1.00]\\
$Distraction - Distancing$ & -4.61 & 16.14 & 45.00 & -0.29 & 1.00 & 0.26 & 1.81e-03 & {}[0.00, 1.00]\\
$Distraction - Suppression$ & -25.49 & 16.14 & 45.00 & -1.58 & 0.73 & 0.77 & 0.05 & {}[0.00, 1.00]\\
$Distancing - Suppression$ & -20.88 & 16.14 & 45.00 & -1.29 & 1.00 & 0.52 & 0.04 & {}[0.00, 1.00]\\
\bottomrule
\addlinespace
\end{tabular}

\begin{tablenotes}[para]
\normalsize{\textit{Note.} $SE$ = standard error, $df$ = degrees of freedom, $t$ = $t$-statistic, $p$ = $p$-value, CI = confidence interval.}
\end{tablenotes}

\end{threeparttable}
\end{center}

\end{table}
Figure:
\begin{figure}[H]
\includegraphics[width=0.75\linewidth]{Manuscript_ERED_Stage1_files/figure-latex/FigSubjArousalRegPilot-1} \caption{Subjective arousal ratings for the conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression" visualized as boxplots. Each dot represents the effort rating of a single subject. Bold dots represent outliers.}(\#fig:FigSubjArousalRegPilot)
\end{figure}
## Pilot study: Physiological responding (*Corrugator* and *Levator* activity) in the conditions "Active viewing - neutral" and "Active viewing - negative"
*Corrugator*:
ANOVA: 

\begin{tabular}{l|l|l|l|l|l}
\hline
Effect & df & MSE & F & ges & p.value\\
\hline
block & 1, 15 & 1.01 & 9.70 ** & .237 & .007\\
\hline
\end{tabular}


$BF10=$ 6,690,401.91

Paired contrasts:

\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:unnamed-chunk-5}Paired contrasts for the rmANOVA comparing physiological responding (Corrugator activity) of negative and neutral pictures in the condition "active viewing".}

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{neutral} - View_{negative}$ & -1.11 & 0.36 & 15.00 & -3.11 & 0.01 & 5,019,313.20 & 0.39 & {}[0.09, 1.00]\\
\bottomrule
\addlinespace
\end{tabular}

\begin{tablenotes}[para]
\normalsize{\textit{Note.} $SE$ = standard error, $df$ = degrees of freedom, $t$ = $t$-statistic, $p$ = $p$-value, CI = confidence interval.}
\end{tablenotes}

\end{threeparttable}
\end{center}

\end{table}
*Levator*:
ANOVA: 

\begin{tabular}{l|l|l|l|l|l}
\hline
Effect & df & MSE & F & ges & p.value\\
\hline
block & 1, 15 & 0.17 & 7.72 * & .162 & .014\\
\hline
\end{tabular}


$BF10=$ 48.44

Paired contrasts:

\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:unnamed-chunk-6}Paired contrasts for the rmANOVA comparing physiological responding (Levator activity) of negative and neutral pictures in the condition "active viewing".}

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{neutral} - View_{negative}$ & -0.40 & 0.14 & 15.00 & -2.78 & 0.01 & 41.02 & 0.34 & {}[0.05, 1.00]\\
\bottomrule
\addlinespace
\end{tabular}

\begin{tablenotes}[para]
\normalsize{\textit{Note.} $SE$ = standard error, $df$ = degrees of freedom, $t$ = $t$-statistic, $p$ = $p$-value, CI = confidence interval.}
\end{tablenotes}

\end{threeparttable}
\end{center}

\end{table}
Figures:
\begin{figure}[H]
\includegraphics[width=0.75\linewidth]{Manuscript_ERED_Stage1_files/figure-latex/FigEMGCorrViewPilot-1} \caption{Corrugator activity for the conditions "Active viewing - neutral" and "Active viewing - negative" visualized as boxplots. Each dot represents the corrugator activity of a single trial. Bold dots represent outliers.}(\#fig:FigEMGCorrViewPilot)
\end{figure}
\begin{figure}[H]
\includegraphics[width=0.75\linewidth]{Manuscript_ERED_Stage1_files/figure-latex/FigEMGLevViewPilot-1} \caption{Levator activity for the conditions "Active viewing - neutral" and "Active viewing - negative" visualized as boxplots. Each dot represents the levator activity of a single trial. Bold dots represent outliers.}(\#fig:FigEMGLevViewPilot)
\end{figure}
## Pilot study: Physiological responding (*Corrugator* and *Levator* activity) in the conditions"Active viewing - negative", "Distraction", "Distancing", and "Suppression"
*Corrugator*:
ANOVA: 

\begin{tabular}{l|l|l|l|l|l}
\hline
Effect & df & MSE & F & ges & p.value\\
\hline
block & 1.53, 22.98 & 1.16 & 5.71 * & .189 & .015\\
\hline
\end{tabular}


$BF10=$ 5,257,689.54

Paired contrasts:

\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:unnamed-chunk-7}Paired contrasts for the rmANOVA comparing physiological responding (Corrugator activity) of conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression".}

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{negative} - Distraction$ & 0.88 & 0.27 & 45.00 & 3.22 & 0.01 & 4,962.89 & 0.19 & {}[0.05, 1.00]\\
$View_{negative} - Distancing$ & 0.95 & 0.27 & 45.00 & 3.50 & 0.01 & 616.63 & 0.21 & {}[0.06, 1.00]\\
$View_{negative} - Suppression$ & 0.92 & 0.27 & 45.00 & 3.40 & 0.01 & 11,678.82 & 0.20 & {}[0.06, 1.00]\\
$Distraction - Distancing$ & 0.08 & 0.27 & 45.00 & 0.28 & 1.00 & 0.07 & 1.78e-03 & {}[0.00, 1.00]\\
$Distraction - Suppression$ & 0.05 & 0.27 & 45.00 & 0.18 & 1.00 & 0.08 & 7.22e-04 & {}[0.00, 1.00]\\
$Distancing - Suppression$ & -0.03 & 0.27 & 45.00 & -0.10 & 1.00 & 0.06 & 2.36e-04 & {}[0.00, 1.00]\\
\bottomrule
\addlinespace
\end{tabular}

\begin{tablenotes}[para]
\normalsize{\textit{Note.} $SE$ = standard error, $df$ = degrees of freedom, $t$ = $t$-statistic, $p$ = $p$-value, CI = confidence interval.}
\end{tablenotes}

\end{threeparttable}
\end{center}

\end{table}
*Levator*:
ANOVA: 

\begin{tabular}{l|l|l|l|l|l}
\hline
Effect & df & MSE & F & ges & p.value\\
\hline
block & 2.07, 31.00 & 0.20 & 8.27 ** & .225 & .001\\
\hline
\end{tabular}


$BF10=$ 672,341.29

Paired contrasts:

\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:unnamed-chunk-8}Paired contrasts for the rmANOVA comparing physiological respodning (Levator activity) of conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression".}

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{negative} - Distraction$ & 0.42 & 0.13 & 45.00 & 3.24 & 0.01 & 58.02 & 0.19 & {}[0.05, 1.00]\\
$View_{negative} - Distancing$ & 0.45 & 0.13 & 45.00 & 3.46 & 0.01 & 93.49 & 0.21 & {}[0.06, 1.00]\\
$View_{negative} - Suppression$ & 0.62 & 0.13 & 45.00 & 4.79 & 0.00 & 6,253.91 & 0.34 & {}[0.16, 1.00]\\
$Distraction - Distancing$ & 0.03 & 0.13 & 45.00 & 0.22 & 1.00 & 0.07 & 1.06e-03 & {}[0.00, 1.00]\\
$Distraction - Suppression$ & 0.20 & 0.13 & 45.00 & 1.54 & 0.78 & 1.52 & 0.05 & {}[0.00, 1.00]\\
$Distancing - Suppression$ & 0.17 & 0.13 & 45.00 & 1.32 & 1.00 & 0.52 & 0.04 & {}[0.00, 1.00]\\
\bottomrule
\addlinespace
\end{tabular}

\begin{tablenotes}[para]
\normalsize{\textit{Note.} $SE$ = standard error, $df$ = degrees of freedom, $t$ = $t$-statistic, $p$ = $p$-value, CI = confidence interval.}
\end{tablenotes}

\end{threeparttable}
\end{center}

\end{table}
Figures:
\begin{figure}[H]
\includegraphics[width=0.75\linewidth]{Manuscript_ERED_Stage1_files/figure-latex/FigEMGCorrRegPilot-1} \caption{Corrugator activity for the conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression" visualized as boxplots. Each dot represents the corrugator activity of a single trial. Bold dots represent outliers.}(\#fig:FigEMGCorrRegPilot)
\end{figure}
\begin{figure}[H]
\includegraphics[width=0.75\linewidth]{Manuscript_ERED_Stage1_files/figure-latex/FigEMGLevRegPilot-1} \caption{Levator activity for the conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression" visualized as boxplots. Each dot represents the levator activity of a single trial. Bold dots represent outliers.}(\#fig:FigEMGLevRegPilot)
\end{figure}
## Pilot study: Subjective effort in the conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression"
ANOVA:

\begin{tabular}{l|l|l|l|l|l}
\hline
Effect & df & MSE & F & ges & p.value\\
\hline
block & 2.38, 35.66 & 4388.19 & 11.13 *** & .185 & <.001\\
\hline
\end{tabular}


$BF10=$ 7.40

Paired contrasts:

\begin{table}[H]

\begin{center}
\begin{threeparttable}

\caption{\label{tab:unnamed-chunk-9}Paired contrasts for the rmANOVA comparing subjective effort of conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression".}

\begin{tabular}{lllllllll}
\toprule
Contrast & \multicolumn{1}{c}{Estimate} & \multicolumn{1}{c}{$SE$} & \multicolumn{1}{c}{$df$} & \multicolumn{1}{c}{$t$} & \multicolumn{1}{c}{$p$} & \multicolumn{1}{c}{$BF10$} & \multicolumn{1}{c}{$\eta_{p}^{2}$} & \multicolumn{1}{c}{$95\% CI$}\\
\midrule
$View_{negative} - Distancing$ & -110.72 & 20.85 & 45.00 & -5.31 & 0.00 & 59.77 & 0.39 & {}[0.20, 1.00]\\
$View_{negative} - Distraction$ & -89.72 & 20.85 & 45.00 & -4.30 & 0.00 & 20.49 & 0.29 & {}[0.12, 1.00]\\
$View_{negative} - Suppression$ & -88.15 & 20.85 & 45.00 & -4.23 & 0.00 & 33.13 & 0.28 & {}[0.11, 1.00]\\
$Distraction - Distancing$ & 21.00 & 20.85 & 45.00 & 1.01 & 1.00 & 0.50 & 0.02 & {}[0.00, 1.00]\\
$Distraction - Suppression$ & 22.57 & 20.85 & 45.00 & 1.08 & 1.00 & 0.57 & 0.03 & {}[0.00, 1.00]\\
$Distancing - Suppression$ & 1.57 & 20.85 & 45.00 & 0.08 & 1.00 & 0.26 & 1.27e-04 & {}[0.00, 1.00]\\
\bottomrule
\addlinespace
\end{tabular}

\begin{tablenotes}[para]
\normalsize{\textit{Note.} $SE$ = standard error, $df$ = degrees of freedom, $t$ = $t$-statistic, $p$ = $p$-value, CI = confidence interval.}
\end{tablenotes}

\end{threeparttable}
\end{center}

\end{table}
Figure:
\begin{figure}[H]
\includegraphics[width=0.75\linewidth]{Manuscript_ERED_Stage1_files/figure-latex/FigSubjEffortPilot-1} \caption{Subjective effort ratings for the conditions "Active viewing - negative", "Distraction", "Distancing", and "Suppression" visualized as boxplots. Each dot represents the effort rating of a single subject. Bold dots represent outliers.}(\#fig:FigSubjEffortPilot)
\end{figure}

