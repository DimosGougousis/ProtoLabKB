---
type: knowledge-article
category: compliance
source_url: https://www.pmddtc.state.gov/ddtc_public?id=ddtc_kb_article_page&sys_id=24d528fddbfc930044f9ff621f961987
fetched_at: 2026-04-21
summary: ITAR and EAR export control requirements specific to additive manufacturing, including deemed export rules for 3D printing files, technical data restrictions, foreign national access controls, and end-use certificate requirements for defense-related printed parts.
---

# Additive Manufacturing Export Controls

## Overview

Additive manufacturing (3D printing) presents unique export control challenges due to the digital nature of design files and the ability to produce functional parts directly from digital data. This article covers ITAR and EAR requirements specific to AM processes.

## ITAR (International Traffic in Arms Regulations)

### Applicability to 3D Printing

ITAR applies to defense-related articles, technical data, and services, including:
- Defense articles on the US Munitions List (USML)
- Technical data related to defense articles
- Defense services

**ProtoLabs Status:** ITAR Registered (valid through 2026)

### ITAR Requirements for 3D Printed Defense Parts

| Requirement | Description | Implementation |
|-------------|-------------|----------------|
| **Facility Registration** | Manufacturing must occur in ITAR-registered facility | NC Morrisville facility (DMLS only) |
| **Personnel Restrictions** | No foreign nationals may access ITAR-controlled designs | US persons only for ITAR jobs |
| **Technical Data Control** | CAD files, STL, 3MF must be marked and secured | Encrypted storage, access logs |
| **End-Use Certificate** | Documentation of final application may be required | Customer-provided EUC |
| **Access Logging** | All access to ITAR data must be recorded | Audit trail maintained |

### Deemed Export Considerations for AM

**What Constitutes a Deemed Export in 3D Printing:**
- Sharing CAD files with foreign nationals (even in the US)
- Providing technical assistance on defense-related designs
- Releasing manufacturing parameters for ITAR-controlled parts
- Allowing foreign national access to AM equipment configured for defense parts

**Technical Data Restrictions:**
| Data Type | ITAR Status | Notes |
|-----------|-------------|-------|
| STL/3MF files for defense parts | Controlled | ITAR technical data |
| CAD files (STEP, IGES) for defense | Controlled | ITAR technical data |
| Build parameters for defense parts | Controlled | May be technical data |
| Generic material properties | Uncontrolled | Public domain information |
| Standard design rules | Uncontrolled | Public domain information |

### Country Restrictions for ITAR Exports

ITAR generally prohibits exports to:
- Proscribed countries (embargoed nations)
- Countries subject to arms embargoes
- Certain end-users on restricted lists

**Note:** ITAR does not have a "de minimis" exception. Even small quantities or prototype parts are controlled.

## EAR (Export Administration Regulations)

### Applicability to Additive Manufacturing

EAR applies to dual-use items (commercial items with potential military application) and items on the Commerce Control List (CCL).

**Classification:** Most 3D printed parts fall under **EAR99** (no license required)

### When EAR Licensing May Be Required

| Scenario | EAR Classification | License Requirement |
|----------|-------------------|---------------------|
| Standard commercial parts | EAR99 | No license required |
| Parts for restricted end-users | Varies | Entity List restrictions apply |
| Parts for embargoed countries | Varies | Country-based restrictions |
| Defense-related applications | Varies | Defense End-Use Statement |
| Aerospace components with specific ECCNs | 9A610, 9A619 | May require license |
| Advanced materials (certain ceramics) | 1C107, 1C991 | May require license |

### Deemed Export Rules (EAR)

**Foreign National Access:**
- Release of technology to foreign nationals in the US is a deemed export
- Applies to technology controlled under ECCNs
- Most 3D printing technology is EAR99 (not controlled)

**Technical Data Under EAR:**
| Data Type | EAR Status | Notes |
|-----------|------------|-------|
| Generic AM process parameters | EAR99 | Publicly available |
| Material datasheets | EAR99 | Publicly available |
| Custom process development | EAR99 | Generally not controlled |
| Controlled technical data | Specific ECCN | Rare for standard AM |

## End-Use Certificate Requirements

### When End-Use Certificates Are Required

| Scenario | Certificate Type | Required Documentation |
|----------|------------------|------------------------ |
| ITAR-controlled parts | ITAR End-Use Certificate | End-user, end-use, country |
| EAR-controlled items | End-User Statement | End-user, intended application |
| Restricted countries | Enhanced screening | Additional due diligence |
| Defense-related applications | Defense End-Use Statement | Military end-use attestation |

### End-Use Certificate Content

A typical end-use certificate for 3D printed defense parts includes:
1. **End-User Information:** Company name, address, contact
2. **End-Use Description:** Specific application of the part
3. **Country of Ultimate Destination:** Final destination country
4. **Re-Export Restrictions:** Agreement not to re-export without authorization
5. **Compliance Attestation:** Statement of compliance with export controls
6. **Signature and Date:** Authorized signatory

## Best Practices for Export Control Compliance in AM

### Design File Management

1. **Marking:** All ITAR-controlled files must be marked "ITAR CONTROLLED"
2. **Encryption:** Store ITAR files with encryption at rest
3. **Access Control:** Role-based access with audit logging
4. **Transmission:** Secure file transfer for ITAR data
5. **Retention:** Maintain records per ITAR requirements (5 years)

### Personnel Practices

1. **Training:** Annual export control training for all employees
2. **Citizenship Verification:** Confirm US person status for ITAR access
3. **Need-to-Know:** Restrict access to job function requirements
4. **Visitor Escort:** Foreign national visitors must be escorted in ITAR areas

### Customer Due Diligence

1. **Screening:** Check customers against restricted party lists
2. **End-Use Verification:** Understand intended application
3. **Country Screening:** Verify destination is not embargoed
4. **Documentation:** Maintain records of due diligence

## Summary

Export control compliance for additive manufacturing requires careful attention to:
- **ITAR controls** for defense-related parts and technical data
- **Deemed export rules** for foreign national access
- **End-use certificates** for defense applications
- **File marking and control** for ITAR technical data
- **Personnel practices** to prevent unauthorized access

ProtoLabs maintains ITAR registration and implements comprehensive export control procedures to ensure compliant manufacturing of defense-related 3D printed parts.
---
type: knowledge-article
category: compliance
source_url: https://www.pmddtc.state.gov/ddtc_public?id=ddtc_kb_article_page&sys_id=24d528fddbfc930044f9ff621f961987
fetched_at: 2026-04-21
summary: ITAR and EAR export control requirements specific to additive manufacturing, including deemed export rules for 3D printing files, technical data restrictions, foreign national access controls, and end-use certificate requirements for defense-related printed parts.
---

# Additive Manufacturing Export Controls

## Overview

Additive manufacturing (3D printing) presents unique export control challenges due to the digital nature of design files and the ability to produce functional parts directly from digital data. This article covers ITAR and EAR requirements specific to AM processes.

## ITAR (International Traffic in Arms Regulations)

### Applicability to 3D Printing

ITAR applies to defense-related articles, technical data, and services, including:
- Defense articles on the US Munitions List (USML)
- Technical data related to defense articles
- Defense services

**ProtoLabs Status:** ITAR Registered (valid through 2026)

### ITAR Requirements for 3D Printed Defense Parts

| Requirement | Description | Implementation |
|-------------|-------------|----------------|
| **Facility Registration** | Manufacturing must occur in ITAR-registered facility | NC Morrisville facility (DMLS only) |
| **Personnel Restrictions** | No foreign nationals may access ITAR-controlled designs | US persons only for ITAR jobs |
| **Technical Data Control** | CAD files, STL, 3MF must be marked and secured | Encrypted storage, access logs |
| **End-Use Certificate** | Documentation of final application may be required | Customer-provided EUC |
| **Access Logging** | All access to ITAR data must be recorded | Audit trail maintained |

### Deemed Export Considerations for AM

**What Constitutes a Deemed Export in 3D Printing:**
- Sharing CAD files with foreign nationals (even in the US)
- Providing technical assistance on defense-related designs
- Releasing manufacturing parameters for ITAR-controlled parts
- Allowing foreign national access to AM equipment configured for defense parts

**Technical Data Restrictions:**
| Data Type | ITAR Status | Notes |
|-----------|-------------|-------|
| STL/3MF files for defense parts | Controlled | ITAR technical data |
| CAD files (STEP, IGES) for defense | Controlled | ITAR technical data |
| Build parameters for defense parts | Controlled | May be technical data |
| Generic material properties | Uncontrolled | Public domain information |
| Standard design rules | Uncontrolled | Public domain information |

### Country Restrictions for ITAR Exports

ITAR generally prohibits exports to:
- Proscribed countries (embargoed nations)
- Countries subject to arms embargoes
- Certain end-users on restricted lists

**Note:** ITAR does not have a "de minimis" exception. Even small quantities or prototype parts are controlled.

## EAR (Export Administration Regulations)

### Applicability to Additive Manufacturing

EAR applies to dual-use items (commercial items with potential military application) and items on the Commerce Control List (CCL).

**Classification:** Most 3D printed parts fall under **EAR99** (no license required)

### When EAR Licensing May Be Required

| Scenario | EAR Classification | License Requirement |
|----------|-------------------|---------------------|
| Standard commercial parts | EAR99 | No license required |
| Parts for restricted end-users | Varies | Entity List restrictions apply |
| Parts for embargoed countries | Varies | Country-based restrictions |
| Aerospace components with specific ECCNs | 9A610, 9A619 | May require license |
| Advanced materials (certain ceramics) | 1C107, 1C991 | May require license |

### Deemed Export Rules (EAR)

**Foreign National Access:**
- Release of technology to foreign nationals in the US is a deemed export
- Applies to technology controlled under ECCNs
- Most 3D printing technology is EAR99 (not controlled)

**Technical Data Under EAR:**
| Data Type | EAR Status | Notes |
|-----------|------------|-------|
| Generic AM process parameters | EAR99 | Publicly available |
| Material datasheets | EAR99 | Publicly available |
| Custom process development | EAR99 | Generally not controlled |
| Controlled technical data | Specific ECCN | Rare for standard AM |

## End-Use Certificate Requirements

### When End-Use Certificates Are Required

| Scenario | Certificate Type | Required Documentation |
|----------|------------------|------------------------ |
| ITAR-controlled parts | ITAR End-Use Certificate | End-user, end-use, country |
| EAR-controlled items | End-User Statement | End-user, intended application |
| Restricted countries | Enhanced screening | Additional due diligence |
| Defense-related applications | Defense End-Use Statement | Military end-use attestation |

### End-Use Certificate Content

A typical end-use certificate for 3D printed defense parts includes:
1. **End-User Information:** Company name, address, contact
2. **End-Use Description:** Specific application of the part
3. **Country of Ultimate Destination:** Final destination country
4. **Re-Export Restrictions:** Agreement not to re-export without authorization
5. **Compliance Attestation:** Statement of compliance with export controls
6. **Signature and Date:** Authorized signatory

## Best Practices for Export Control Compliance in AM

### Design File Management

1. **Marking:** All ITAR-controlled files must be marked "ITAR CONTROLLED"
2. **Encryption:** Store ITAR files with encryption at rest
3. **Access Control:** Role-based access with audit logging
4. **Transmission:** Secure file transfer for ITAR data
5. **Retention:** Maintain records per ITAR requirements (5 years)

### Personnel Practices

1. **Training:** Annual export control training for all employees
2. **Citizenship Verification:** Confirm US person status for ITAR access
3. **Need-to-Know:** Restrict access to job function requirements
4. **Visitor Escort:** Foreign national visitors must be escorted in ITAR areas

### Customer Due Diligence

1. **Screening:** Check customers against restricted party lists
2. **End-Use Verification:** Understand intended application
3. **Country Screening:** Verify destination is not embargoed
4. **Documentation:** Maintain records of due diligence

## Summary

Export control compliance for additive manufacturing requires careful attention to:
- **ITAR controls** for defense-related parts and technical data
- **Deemed export rules** for foreign national access
- **End-use certificates** for defense applications
- **File marking and control** for ITAR technical data
- **Personnel practices** to prevent unauthorized access

ProtoLabs maintains ITAR registration and implements comprehensive export control procedures to ensure compliant manufacturing of defense-related 3D printed parts.
