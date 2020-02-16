/** @jsx jsx */
import { jsx } from "@emotion/core";
import { useParams } from "react-router-dom";
import { format } from "date-fns";
import { Formik, ErrorMessage, FormikErrors } from "formik";
import Button from "@material-ui/core/Button";
import ExpansionPanel from "@material-ui/core/ExpansionPanel";
import ExpansionPanelSummary from "@material-ui/core/ExpansionPanelSummary";
import ExpansionPanelDetails from "@material-ui/core/ExpansionPanelDetails";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import Backdrop from "@material-ui/core/Backdrop";
import CircularProgress from "@material-ui/core/CircularProgress";
import {
  backdrop,
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
// import { baseApiUrl } from "../api/api";
// import ProgramList from "./ProgramList";

interface ClientDetailsProps {
  client: Types.Client;
  programList: Types.Program[];
  onFormSubmit: (
    client_code: string,
    program_completion: number,
    returned_to_care: number,
    program_significantly_modified: number
  ) => void;
  isLoading: boolean;
  hasError: boolean;
  error: string;
  program_completion_response: string | null;
}

interface FormValues {
  Program_Completion: number | null;
  Returned_to_Care: number | null;
  program_significantly_modified: number | null;
}

const ClientDetails: React.FC<ClientDetailsProps> = props => {
  let { index } = useParams();
  if (!index) {
    return <h1 css={subHeading}>No client found</h1>;
  }
  const { client } = props;
  if (!client || !client.client_code) {
    return <h1 css={subHeading}>No client found</h1>;
  }

  const initialValues: FormValues = {
    Program_Completion: client.Program_Completion,
    Returned_to_Care: client.Returned_to_Care,
    program_significantly_modified: client.program_significantly_modified
  };
  // let referred_program: Types.Program | undefined = undefined;
  // if (client.referred_program) {
  //   referred_program = props.programList.find(
  //     c => client.referred_program === c.program.toString()
  //   );
  // }
  return (
    <div css={wrap}>
      <div css={mainContent}>
        <Backdrop css={backdrop} open={props.isLoading}>
          <CircularProgress color="inherit" />
        </Backdrop>
        {/* <div style={{ textAlign: "right" }}>
          <a
            rel="noopener noreferrer"
            target="_blank"
            css={txtDetail}
            href={`${baseApiUrl}/index/${client.client_code}`}
          >
            Download PDF Report
          </a>
        </div> */}
        <ExpansionPanel defaultExpanded>
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
                <div css={txtDetail}>
                  {client.episode_start
                    ? format(new Date(client.episode_start), "MM-dd-yyyy")
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Previously Referred</label>
                <div css={txtDetail}>
                  {Types.episode_number[Number(client.episode_number)]}
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
                <div css={txtDetail}>
                  {client.dob ? format(new Date(client.dob), "MM-dd-yyyy") : ""}
                </div>
              </div>
              <div css={twoCol} style={{ width: 60 }}>
                <label css={txtLabel}>Age</label>
                <div css={txtDetail}>{client.age}</div>
              </div>
              <div css={twoCol} style={{ width: "39%" }}>
                <label css={txtLabel}>Sex</label>
                <div css={txtDetail}>
                  {client.gender ? Types.gender[Number(client.gender)] : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Primary Language</label>
                <div css={txtDetail}>
                  {Types.primary_language[Number(client.primary_language)]}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Referral Source</label>
                <div css={txtDetail}>
                  {Types.RefSourceCode[Number(client.RefSourceCode)]}
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
                  {client.CYF_code !== null
                    ? Types.CYF_code[client.CYF_code]
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
                  {client.number_of_foster_care_placements !== null
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
                  {client.number_of_prior_AWOLS !== null
                    ? Types.number_of_prior_AWOLS[client.number_of_prior_AWOLS]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Total Prior Placement Terminations</label>
                <div css={txtDetail}>
                  {client.number_of_prior_treatment_terminations !== null
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
                  {client.termination_directly_to_AV !== null
                    ? Types.termination_directly_to_AV[
                        client.termination_directly_to_AV
                      ]
                    : "NA"}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Time since living at home</label>
                <div css={txtDetail}>
                  <div css={txtDetail}>
                    {client.length_of_time_since_living_at_home !== null
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
                  {Types.radioValues[Number(client.hist_of_prior_program_SAO)]}
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
                  {Types.radioValues[Number(client.autism_Diagnosis)]}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Borderline Personality Disorder</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.borderline_Personality)]}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>RAD</label>
                <div css={txtDetail}>
                  {
                    Types.radioValues[
                      Number(client.reactive_Attachment_Disorder)
                    ]
                  }
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Animal Cruelty</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.animal_cruelty)]}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Schizophrenia</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.schizophrenia)]}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Psychosis</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.psychosis)]}
                </div>
              </div>
            </div>

            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>IQ</label>
                <div css={txtDetail}>
                  {Types.borderline_IQ[Number(client.borderline_IQ)]}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
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
                  {client.prior_hospitalizations !== null
                    ? client.prior_hospitalizations
                    : ""}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Time since last hospitalization</label>
                <div css={txtDetail}>
                  {client.severe_mental_health_symptoms !== null
                    ? Types.severe_mental_health_symptoms[
                        client.severe_mental_health_symptoms
                      ]
                    : ""}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Medication Compliant</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.compliant_with_meds)]}
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
                  {Types.radioValues[Number(client.incarcerated_caregivers)]}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Deceased Caregiver</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.death_Caregiver)]}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Incarcerated Siblings</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.incarcerated_siblings)]}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Deceased Siblings</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.death_Silblings)]}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Alcohol Use</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.alcohol_Use)]}
                </div>
              </div>
              <div css={twoCol}>
                <label css={txtLabel}>Drug Use</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.drug_Use)]}
                </div>
              </div>
            </div>
            <div css={fieldRow}>
              <div css={twoCol}>
                <label css={txtLabel}>Abuse/Neglect</label>
                <div css={txtDetail}>
                  {Types.radioValues[Number(client.abuse_neglect)]}
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
            <div css={txtDetail}>{client.client_selected_program}</div>
          </div>
        </div>

        <Formik
          initialValues={initialValues}
          enableReinitialize
          validate={values => {
            const errors: FormikErrors<FormValues> = {};
            if (values.Program_Completion === null) {
              errors.Program_Completion = "Required";
            }
            if (values.Returned_to_Care === null) {
              errors.Returned_to_Care = "Required";
            }
            if (values.program_significantly_modified === null) {
              errors.program_significantly_modified = "Required";
            }
            return errors;
          }}
          onSubmit={async (values, helpers) => {
            if (
              !client.client_code ||
              values.Program_Completion === null ||
              values.Returned_to_Care === null ||
              values.program_significantly_modified === null
            ) {
              return false;
            }
            await props.onFormSubmit(
              client.client_code,
              Number(values.Program_Completion),
              Number(values.Returned_to_Care),
              Number(values.program_significantly_modified)
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
                      checked={
                        values.Program_Completion !== null
                          ? Number(values.Program_Completion) === 1
                          : false
                      }
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
                      checked={
                        values.Program_Completion !== null
                          ? Number(values.Program_Completion) === 0
                          : false
                      }
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
                      checked={
                        values.Returned_to_Care !== null
                          ? Number(values.Returned_to_Care) === 1
                          : false
                      }
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
                      checked={
                        values.Returned_to_Care !== null
                          ? Number(values.Returned_to_Care) === 0
                          : false
                      }
                    />{" "}
                    <label htmlFor="Returned_to_Care-no">No</label>
                  </div>
                  <ErrorMessage component="span" name="Returned_to_Care" />
                </div>
              </div>
              <div css={fieldRow}>
                <div css={twoCol}>
                  <label css={txtLabel}>
                    Was the program significantly modified to treat this client?
                  </label>
                  <div css={fieldBox}>
                    <input
                      type="radio"
                      onChange={handleChange}
                      name="program_significantly_modified"
                      id="program_significantly_modified-yes"
                      value="1"
                      checked={
                        values.program_significantly_modified !== null
                          ? Number(values.program_significantly_modified) === 1
                          : false
                      }
                    />{" "}
                    <label htmlFor="program_significantly_modified-yes">
                      Yes
                    </label>
                  </div>
                  <div css={fieldBox}>
                    <input
                      type="radio"
                      onChange={handleChange}
                      name="program_significantly_modified"
                      id="program_significantly_modified-no"
                      value="0"
                      checked={
                        values.program_significantly_modified !== null
                          ? Number(values.program_significantly_modified) === 0
                          : false
                      }
                    />{" "}
                    <label htmlFor="program_significantly_modified-no">
                      No
                    </label>
                  </div>
                  <ErrorMessage
                    component="span"
                    name="program_significantly_modified"
                  />
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
