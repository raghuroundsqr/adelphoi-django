/** @jsx jsx */
import { jsx } from "@emotion/core";
import { useParams } from "react-router-dom";
import { Formik, ErrorMessage, FormikErrors } from "formik";
import Button from "@material-ui/core/Button";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import {
  wrap,
  subHeading,
  fieldRow,
  mainContent,
  twoCol,
  txtLabel,
  panel,
  panelHeading,
  panelHeader,
  txtDetail,
  fieldBox
} from "./styles";
import * as Types from "../api/definitions";

interface ClientDetailsProps {
  clientList: Types.Client[];
  onFormSubmit: (
    client_code: string,
    program_completion: string,
    returned_to_care: string
  ) => void;
  isLoading: boolean;
  hasError: boolean;
  error: string;
  program_completion_response: string | null;
}

interface FormValues {
  Program_Completion: string;
  Returned_to_Care: string;
}

const initialValues: FormValues = {
  Program_Completion: "",
  Returned_to_Care: ""
};

const ClientDetails: React.FC<ClientDetailsProps> = props => {
  let { index } = useParams();
  if (!index) {
    return <h1 css={subHeading}>No client found</h1>;
  }
  const client = props.clientList[Number(index)];
  if (!client) {
    return <h1 css={subHeading}>No client found</h1>;
  }

  return (
    <div css={wrap}>
      <div css={mainContent}>
        <ExpansionPanel expanded>
          <ExpansionPanelSummary
            css={panelHeader}
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
          >
            <h1 css={panelHeading}>Demographics</h1>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails css={panel}>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Date of Referral</label>
                <div css={txtDetail}>{client.episode_start}</div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Previously Referred</label>
                <div css={txtDetail}>
                  {client.episode_number
                    ? Types.episode_number[client.episode_number]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Client Code/ID</label>
                <div css={txtDetail}>{client.client_code}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>First Name</label>
                <div css={txtDetail}>{client.name}</div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Last Name</label>
                <div css={txtDetail}>{client.last_name}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>DOB</label>
                <div css={txtDetail}>{client.dob}</div>
              </div>
              <div css={twoCol} style={{ width: 60 }}>
                <label css={txtLabel}>Age</label>
                <div css={txtDetail}>{client.age}</div>
              </div>
              <div css={twoCol} style={{ width: "39%" }}>
                <label css={txtLabel}>Sex</label>
                <div css={txtDetail}>
                  {client.gender ? Types.gender[client.gender] : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Primary Language</label>
                <div css={txtDetail}>
                  {client.primary_language
                    ? Types.primary_language[client.primary_language]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Referral Source</label>
                <div css={txtDetail}>
                  {client.RefSourceCode
                    ? Types.RefSourceCode[client.RefSourceCode]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Legal Status</label>

                <div css={txtDetail}>
                  {client.ls_type ? Types.ls_type[client.ls_type] : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>C & Y Involvement</label>

                <div css={txtDetail}>
                  {client.CYF_code ? Types.radioValues[client.CYF_code] : ""}
                </div>
              </div>
            </div>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel>
          <ExpansionPanelSummary
            css={panelHeader}
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
          >
            <h1 css={panelHeading}>Placement History</h1>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails css={panel}>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Number of prior placements</label>
                <div css={txtDetail}>
                  {client.number_of_prior_placements
                    ? Types.number_of_prior_placements[
                        client.number_of_prior_placements
                      ]
                    : "NA"}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Number of prior foster homes</label>
                <div css={txtDetail}>
                  {client.number_of_foster_care_placements
                    ? Types.number_of_foster_care_placements[
                        client.number_of_foster_care_placements
                      ]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>History of AWOLS</label>
                <div css={txtDetail}>
                  {client.number_of_prior_AWOLS
                    ? Types.number_of_prior_AWOLS[client.number_of_prior_AWOLS]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Total Prior Placement Terminations</label>
                <div css={txtDetail}>
                  {client.number_of_prior_treatment_terminations
                    ? Types.number_of_prior_treatment_terminations[
                        client.number_of_prior_treatment_terminations
                      ]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>
                  Terminations directly before referred
                </label>
                <div css={txtDetail}>
                  {client.termination_directly_to_AV
                    ? Types.termination_directly_to_AV[
                        client.termination_directly_to_AV
                      ]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Time since living at home</label>
                <div css={txtDetail}>
                  <div css={txtDetail}>
                    {client.length_of_time_since_living_at_home
                      ? Types.length_of_time_since_living_at_home[
                          client.length_of_time_since_living_at_home
                        ]
                      : ""}
                  </div>
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>
                  Sexually Acting Out behaviors in Placement
                </label>
                <div css={txtDetail}>
                  {client.hist_of_prior_program_SAO
                    ? Types.radioValues[client.hist_of_prior_program_SAO]
                    : "NA"}
                </div>
              </div>
            </div>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel>
          <ExpansionPanelSummary
            css={panelHeader}
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
          >
            <h1 css={panelHeading}>Mental Health</h1>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails css={panel}>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Autism Dx</label>
                <div css={txtDetail}>
                  {client.autism_Diagnosis
                    ? Types.radioValues[client.autism_Diagnosis]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Borderline Personality Disorder</label>
                <div css={txtDetail}>
                  {client.borderline_Personality
                    ? Types.radioValues[client.borderline_Personality]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>RAD</label>
                <div css={txtDetail}>
                  {client.reactive_Attachment_Disorder
                    ? Types.radioValues[client.reactive_Attachment_Disorder]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Animal Cruelty</label>
                <div css={txtDetail}>
                  {client.animal_cruelty
                    ? Types.radioValues[client.animal_cruelty]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Schizophrenia</label>
                <div css={txtDetail}>
                  {client.schizophrenia
                    ? Types.radioValues[client.schizophrenia]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Psychosis</label>
                <div css={txtDetail}>
                  {client.psychosis ? Types.radioValues[client.psychosis] : ""}
                </div>
              </div>
            </div>

            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>
                  &nbsp;
                  <br />
                  IQ
                </label>
                <div css={txtDetail}>{client.borderline_IQ}</div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Significant MH Symptoms Score</label>
                <div css={txtDetail}>
                  {client.significant_mental_health_symptoms}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>
                  Number of Prior MH Hospitalizations
                </label>
                <div css={txtDetail}>
                  {client.severe_mental_health_symptoms
                    ? Types.severe_mental_health_symptoms[
                        client.severe_mental_health_symptoms
                      ]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Time since last hospitalization</label>
                <div css={txtDetail}>
                  {client.severe_mental_health_symptoms}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Medication Compliant</label>
                <div css={txtDetail}>
                  {client.compliant_with_meds
                    ? Types.radioValues[client.compliant_with_meds]
                    : ""}
                </div>
              </div>
            </div>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel>
          <ExpansionPanelSummary
            css={panelHeader}
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
          >
            <h1 css={panelHeading}>Social/Family Hx</h1>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails css={panel}>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Incarcerated Caregiver</label>
                <div css={txtDetail}>
                  {client.incarcerated_caregivers
                    ? Types.radioValues[client.incarcerated_caregivers]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Deceased Caregiver</label>
                <div css={txtDetail}>
                  {client.death_Caregiver
                    ? Types.radioValues[client.death_Caregiver]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Incarcerated Siblings</label>
                <div css={txtDetail}>
                  {client.incarcerated_siblings
                    ? Types.radioValues[client.incarcerated_siblings]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Deceased Siblings</label>
                <div css={txtDetail}>
                  {client.death_Silblings
                    ? Types.radioValues[client.death_Silblings]
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Alcohol Use</label>
                <div css={txtDetail}>
                  {client.alcohol_Use
                    ? Types.radioValues[client.alcohol_Use]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Drug Use</label>
                <div css={txtDetail}>
                  {client.drug_Use ? Types.radioValues[client.drug_Use] : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Abuse/Neglect</label>
                <div css={txtDetail}>
                  {client.abuse_neglect
                    ? Types.radioValues[client.abuse_neglect]
                    : ""}
                </div>
              </div>
            </div>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <ExpansionPanel>
          <ExpansionPanelSummary
            css={panelHeader}
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1a-content"
          >
            <h1 css={panelHeading}>Assessment Scores</h1>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails css={panel}>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>YLS Family Circumstances Score</label>
                <div css={txtDetail}>{client.yls_FamCircumstances_Score}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>YLS Education/Employment Score</label>
                <div css={txtDetail}>{client.yls_Edu_Employ_Score}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>YLS Peer Score</label>
                <div css={txtDetail}>{client.yls_Peer_Score}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>YLS Subab Score</label>
                <div css={txtDetail}>{client.yls_Subab_Score}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>YLS Leisure Score</label>
                <div css={txtDetail}>{client.yls_Leisure_Score}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>YLS Personality Score</label>
                <div css={txtDetail}>{client.yls_Personality_Score}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>YLS Attitude Score</label>
                <div css={txtDetail}>{client.yls_Attitude_Score}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>YLS Prior/Current Offenses Score</label>
                <div css={txtDetail}>
                  {client.yls_PriorCurrentOffenses_Score}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Family Support</label>
                <div css={txtDetail}>{client.family_support}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Fire Setting</label>
                <div css={txtDetail}>{client.fire_setting}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Level of Aggression</label>
                <div css={txtDetail}>{client.level_of_aggression}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Self-Harm</label>
                <div css={txtDetail}>{client.client_self_harm}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Trauma Assessment Score</label>
                <div css={txtDetail}>{client.Screening_tool_Trauma}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>CANS Life Functioning</label>
                <div css={txtDetail}>{client.cans_LifeFunctioning}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>CANS Youth Strengths</label>
                <div css={txtDetail}>{client.cans_YouthStrengths}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>CANS Caregiver Strengths</label>
                <div css={txtDetail}>{client.cans_CareGiverStrengths}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>CANS Culture</label>
                <div css={txtDetail}>{client.cans_Culture}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>CANS Youth Behavior</label>
                <div css={txtDetail}>{client.cans_YouthBehavior}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>CANS Youth Risk</label>
                <div css={txtDetail}>{client.cans_YouthRisk}</div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>CANS Trauma Experience</label>
                <div css={txtDetail}>{client.cans_Trauma_Exp}</div>
              </div>
            </div>
          </ExpansionPanelDetails>
        </ExpansionPanel>

        <h1 css={subHeading}>Referred Program</h1>

        <div css={fieldRow}>
          <div css={twoCol}>
            <div css={txtDetail}>{client.referred_program}</div>
          </div>
        </div>

        <Formik
          initialValues={initialValues}
          enableReinitialize
          validate={values => {
            const errors: FormikErrors<FormValues> = {};
            if (!values.Program_Completion) {
              errors.Program_Completion = "Required";
            }
            if (!values.Returned_to_Care) {
              errors.Returned_to_Care = "Required";
            }
            return errors;
          }}
          onSubmit={async (values, helpers) => {
            console.log(values);
            if (!client.client_code) {
              return false;
            }
            await props.onFormSubmit(
              client.client_code,
              values.Program_Completion,
              values.Returned_to_Care
            );
            // helpers.resetForm();
          }}
        >
          {({ values, handleSubmit, handleChange }) => (
            <form name="clientSearchForm" onSubmit={handleSubmit}>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={txtLabel}>Program Completion</label>
                  <div css={fieldBox}>
                    <input
                      type="radio"
                      onChange={handleChange}
                      name="Program_Completion"
                      id="Program_Completion-yes"
                      value="1"
                      checked={values.Program_Completion === "1"}
                    />{" "}
                    <label htmlFor="Program_Completion-yes">Yes</label>
                  </div>
                  <div css={fieldBox}>
                    <input
                      type="radio"
                      onChange={handleChange}
                      name="Program_Completion"
                      id="Program_Completion-no"
                      value="0"
                      checked={values.Program_Completion === "0"}
                    />{" "}
                    <label htmlFor="Program_Completion-no">No</label>
                  </div>
                  <ErrorMessage component="span" name="Program_Completion" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={txtLabel}>Remained out of care</label>
                  <div css={fieldBox}>
                    <input
                      type="radio"
                      onChange={handleChange}
                      name="Returned_to_Care"
                      id="Returned_to_Care-yes"
                      value="1"
                      checked={values.Returned_to_Care === "1"}
                    />{" "}
                    <label htmlFor="Returned_to_Care-yes">Yes</label>
                  </div>
                  <div css={fieldBox}>
                    <input
                      type="radio"
                      onChange={handleChange}
                      name="Returned_to_Care"
                      id="Returned_to_Care-no"
                      value="0"
                      checked={values.Returned_to_Care === "0"}
                    />{" "}
                    <label htmlFor="Returned_to_Care-no">No</label>
                  </div>
                  <ErrorMessage component="span" name="Returned_to_Care" />
                </div>
              </div>
              <div css={fieldRow} style={{ justifyContent: "flex-end" }}>
                <Button
                  type="submit"
                  size="large"
                  variant="contained"
                  color="primary"
                >
                  Submit
                </Button>
              </div>
            </form>
          )}
        </Formik>
        {props.program_completion_response && (
          <div css={subHeading}>{props.program_completion_response}</div>
        )}
      </div>
      {/* MAIN CONTENT */}
    </div>
  );
};

export default ClientDetails;
