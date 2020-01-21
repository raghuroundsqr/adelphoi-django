import React from "react";
interface iconProps {
  fillColor: string;
}
export const ConfigIcon = (props: iconProps) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="75"
    height="75"
    viewBox="0 0 75 75"
  >
    <path
      fill={props.fillColor}
      fillRule="evenodd"
      d="M64.879,31.1L60.6,30.37a24.179,24.179,0,0,0-1.72-4.154l2.523-3.53a3.757,3.757,0,0,0-.408-4.855l-3.8-3.8a3.741,3.741,0,0,0-2.663-1.109,3.7,3.7,0,0,0-2.179.7L48.81,16.149A23.917,23.917,0,0,0,44.5,14.378l-0.714-4.231A3.764,3.764,0,0,0,40.068,7H34.7a3.764,3.764,0,0,0-3.721,3.147L30.243,14.48A23.571,23.571,0,0,0,26.1,16.226L22.6,13.7a3.764,3.764,0,0,0-4.855.408l-3.81,3.8a3.772,3.772,0,0,0-.408,4.855l2.549,3.581a23.616,23.616,0,0,0-1.695,4.167l-4.231.714A3.764,3.764,0,0,0,7,34.945V40.31a3.764,3.764,0,0,0,3.147,3.721L14.48,44.77a23.593,23.593,0,0,0,1.746,4.142L13.715,52.4a3.757,3.757,0,0,0,.408,4.855l3.8,3.8a3.741,3.741,0,0,0,2.663,1.109,3.7,3.7,0,0,0,2.179-.7l3.581-2.549a24.081,24.081,0,0,0,4.027,1.657l0.714,4.282A3.764,3.764,0,0,0,34.805,68h5.378A3.765,3.765,0,0,0,43.9,64.852l0.726-4.282a24.171,24.171,0,0,0,4.154-1.72l3.53,2.523a3.741,3.741,0,0,0,2.192.7h0a3.741,3.741,0,0,0,2.663-1.109l3.8-3.8a3.772,3.772,0,0,0,.408-4.855l-2.523-3.542a24.01,24.01,0,0,0,1.72-4.154l4.282-.714A3.764,3.764,0,0,0,68,40.182V34.818A3.719,3.719,0,0,0,64.879,31.1Zm-0.293,9.086a0.33,0.33,0,0,1-.28.331l-5.352.892a1.711,1.711,0,0,0-1.376,1.261,20.4,20.4,0,0,1-2.217,5.339,1.723,1.723,0,0,0,.077,1.873l3.147,4.435a0.347,0.347,0,0,1-.038.433l-3.8,3.8a0.324,0.324,0,0,1-.242.1,0.313,0.313,0,0,1-.191-0.064l-4.422-3.147a1.722,1.722,0,0,0-1.873-.077,20.4,20.4,0,0,1-5.339,2.217,1.691,1.691,0,0,0-1.262,1.376l-0.9,5.352a0.33,0.33,0,0,1-.331.28H34.818a0.33,0.33,0,0,1-.331-0.28l-0.892-5.352a1.711,1.711,0,0,0-1.261-1.376,21.179,21.179,0,0,1-5.225-2.141,1.764,1.764,0,0,0-.867-0.229,1.679,1.679,0,0,0-.994.318L20.788,58.7a0.38,0.38,0,0,1-.191.064,0.342,0.342,0,0,1-.242-0.1l-3.8-3.8a0.345,0.345,0,0,1-.038-0.433l3.135-4.4a1.744,1.744,0,0,0,.076-1.886,20.209,20.209,0,0,1-2.243-5.327,1.745,1.745,0,0,0-1.376-1.261l-5.39-.918a0.33,0.33,0,0,1-.28-0.331V34.945a0.33,0.33,0,0,1,.28-0.331l5.314-.892a1.723,1.723,0,0,0,1.389-1.274A20.381,20.381,0,0,1,19.6,27.1a1.7,1.7,0,0,0-.089-1.86l-3.173-4.46a0.347,0.347,0,0,1,.038-0.433l3.8-3.8a0.323,0.323,0,0,1,.242-0.1,0.314,0.314,0,0,1,.191.064l4.4,3.135a1.744,1.744,0,0,0,1.886.076,20.208,20.208,0,0,1,5.327-2.243A1.745,1.745,0,0,0,33.48,16.1l0.918-5.39a0.33,0.33,0,0,1,.331-0.28h5.365a0.33,0.33,0,0,1,.331.28l0.892,5.314a1.722,1.722,0,0,0,1.274,1.389,20.679,20.679,0,0,1,5.467,2.243,1.723,1.723,0,0,0,1.873-.077l4.4-3.16a0.38,0.38,0,0,1,.191-0.064,0.342,0.342,0,0,1,.242.1l3.8,3.8a0.346,0.346,0,0,1,.038.433l-3.148,4.422a1.722,1.722,0,0,0-.076,1.873A20.4,20.4,0,0,1,57.59,32.32a1.691,1.691,0,0,0,1.376,1.262l5.352,0.9a0.33,0.33,0,0,1,.28.331v5.365H64.585ZM37.507,24.33A13.163,13.163,0,1,0,50.67,37.494,13.172,13.172,0,0,0,37.507,24.33Zm0,22.886a9.723,9.723,0,1,1,9.723-9.723A9.729,9.729,0,0,1,37.507,47.216Z"
    />
  </svg>
);

export const NewClientIcon = (props: iconProps) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="75"
    height="75"
    viewBox="0 0 75 75"
  >
    <path
      fill={props.fillColor}
      fillRule="evenodd"
      d="M36.77,40.485h0.421a12.087,12.087,0,0,0,9.268-4.042c5.061-5.752,4.22-15.612,4.128-16.553-0.329-7.064-3.642-10.444-6.376-12.021A14.525,14.525,0,0,0,37.138,6H36.915a14.544,14.544,0,0,0-7.073,1.816c-2.761,1.577-6.126,4.957-6.455,12.074-0.092.941-.933,10.8,4.128,16.553A12.039,12.039,0,0,0,36.77,40.485ZM26.9,20.221c0-.04.013-0.079,0.013-0.106,0.434-9.5,7.125-10.523,9.991-10.523h0.158c3.55,0.079,9.584,1.537,9.991,10.523a0.261,0.261,0,0,0,.013.106c0.013,0.093.933,9.105-3.247,13.85a8.583,8.583,0,0,1-6.77,2.836H36.915a8.555,8.555,0,0,1-6.757-2.836C25.99,29.352,26.884,20.3,26.9,20.221ZM64,56.839V56.8c0-.106-0.013-0.212-0.013-0.331-0.079-2.624-.25-8.76-5.955-10.722-0.039-.013-0.092-0.026-0.132-0.04A37.8,37.8,0,0,1,46.985,40.7a1.764,1.764,0,0,0-2.471.438,1.8,1.8,0,0,0,.434,2.492,40.8,40.8,0,0,0,12,5.527c3.063,1.1,3.405,4.4,3.5,7.422a2.676,2.676,0,0,0,.013.331,24.247,24.247,0,0,1-.276,4.1c-2.13,1.219-10.478,5.434-23.177,5.434-12.647,0-21.047-4.228-23.19-5.447a22.942,22.942,0,0,1-.276-4.1c0-.106.013-0.212,0.013-0.331,0.092-3.022.434-6.322,3.5-7.422a41.19,41.19,0,0,0,12-5.527,1.8,1.8,0,0,0,.434-2.492,1.764,1.764,0,0,0-2.471-.437A37.4,37.4,0,0,1,16.1,45.694c-0.053.013-.092,0.026-0.131,0.04-5.706,1.975-5.876,8.111-5.955,10.722a2.671,2.671,0,0,1-.013.331v0.04a20.482,20.482,0,0,0,.671,6,1.7,1.7,0,0,0,.684.835C11.752,63.93,21.2,70,37.02,70s25.267-6.084,25.662-6.335a1.769,1.769,0,0,0,.684-0.835A21.49,21.49,0,0,0,64,56.839Z"
    />
    />
  </svg>
);

export const ExistingClientIcon = (props: iconProps) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="75"
    height="75"
    viewBox="0 0 75 75"
  >
    <path
      fill={props.fillColor}
      fillRule="evenodd"
      d="M36.77,40.485h0.421a12.087,12.087,0,0,0,9.268-4.042c5.061-5.752,4.22-15.612,4.128-16.553-0.329-7.064-3.642-10.444-6.376-12.021A14.524,14.524,0,0,0,37.138,6H36.914a14.544,14.544,0,0,0-7.073,1.816c-2.761,1.577-6.126,4.957-6.455,12.074-0.092.941-.933,10.8,4.128,16.553A12.038,12.038,0,0,0,36.77,40.485ZM26.9,20.221c0-.04.013-0.079,0.013-0.106,0.434-9.5,7.125-10.523,9.991-10.523h0.158c3.55,0.079,9.584,1.537,9.991,10.523a0.259,0.259,0,0,0,.013.106c0.013,0.093.933,9.105-3.247,13.85a8.583,8.583,0,0,1-6.77,2.836H36.914a8.555,8.555,0,0,1-6.757-2.836C25.99,29.352,26.884,20.3,26.9,20.221ZM64,56.839V56.8c0-.106-0.013-0.212-0.013-0.331-0.079-2.624-.25-8.76-5.955-10.722-0.039-.013-0.092-0.026-0.131-0.04A37.8,37.8,0,0,1,46.985,40.7a1.764,1.764,0,0,0-2.472.438,1.8,1.8,0,0,0,.434,2.492,40.8,40.8,0,0,0,12,5.527c3.063,1.1,3.4,4.4,3.5,7.422a2.676,2.676,0,0,0,.013.331,24.247,24.247,0,0,1-.276,4.1c-2.13,1.219-10.478,5.434-23.177,5.434-12.647,0-21.047-4.228-23.19-5.447a22.952,22.952,0,0,1-.276-4.1c0-.106.013-0.212,0.013-0.331,0.092-3.022.434-6.322,3.5-7.422a41.189,41.189,0,0,0,12-5.527,1.8,1.8,0,0,0,.434-2.492,1.764,1.764,0,0,0-2.472-.437A37.4,37.4,0,0,1,16.1,45.694c-0.053.013-.092,0.026-0.131,0.04-5.706,1.975-5.876,8.111-5.955,10.722a2.671,2.671,0,0,1-.013.331v0.04a20.482,20.482,0,0,0,.67,6,1.7,1.7,0,0,0,.684.835C11.752,63.93,21.2,70,37.02,70s25.267-6.084,25.662-6.335a1.77,1.77,0,0,0,.684-0.835A21.491,21.491,0,0,0,64,56.839Z"
    />
    <path
      fill={props.fillColor}
      fillRule="evenodd"
      stroke={props.fillColor}
      strokeLinejoin="round"
      strokeWidth="1px"
      d="M43.8,50.179a0.59,0.59,0,0,0-.847,0L35.781,57.5l-2.758-2.815a0.59,0.59,0,0,0-.847,0,0.62,0.62,0,0,0,0,.864L35.357,58.8a0.591,0.591,0,0,0,.847,0l7.6-7.756A0.62,0.62,0,0,0,43.8,50.179Z"
    />
  </svg>
);
