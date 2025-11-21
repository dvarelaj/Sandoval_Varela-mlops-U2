# MLOps End-to-End: Predicción de Enfermedades Comunes y Huérfanas (AWS Edition)

> **Entrega Final - Maestría en IA Aplicada**
> **Autores:** Sandoval & Varela
> **Repositorio:** [Sandoval_Varela-mlops-U2]

## 1. Arquitectura de la Solución

La siguiente arquitectura migra el desarrollo local a un ecosistema Cloud-Native en AWS, garantizando escalabilidad, trazabilidad y gobierno de datos. Se utiliza **GitHub Actions** como orquestador principal de CI/CD, integrando el código existente (FastAPI/Streamlit) con servicios gestionados de ML.

```mermaid
graph LR
    subgraph "CI/CD & Source Control"
        GH[GitHub Repo] -->|Push| GA[GitHub Actions]
        GA -->|Build & Push| ECR[AWS ECR]
        GA -->|Trigger| SM_P[SageMaker Pipeline]
    end

    subgraph "Data Layer (AWS)"
        S3_Raw[(AWS S3 Raw Data)] -->|Ingesta| SM_Proc[SageMaker Processing]
        SM_Proc -->|Datos Limpios| S3_Proc[(AWS S3 Processed)]
        S3_Proc -->|Entrenamiento| SM_Train[SageMaker Training Jobs]
    end

    subgraph "ML Engineering (AWS SageMaker)"
        SM_Train -->|Artifacts| SM_Reg[SageMaker Model Registry]
        SM_Reg -->|Approval| SM_End[Model Artifact]
    end

    subgraph "Deployment & Serving (AWS ECS)"
        ECR -->|Pull Image| ECS_Back[AWS ECS Fargate (FastAPI)]
        ECR -->|Pull Image| ECS_Front[AWS ECS Fargate (Streamlit)]
        SM_End -->|Load Model| ECS_Back
        User((Personal Médico)) -->|HTTPS| ECS_Front
        ECS_Front -->|API Call| ECS_Back
    end

    subgraph "Observability"
        ECS_Back -->|Logs & Metrics| CW[AWS CloudWatch]
        CW -->|Drift Alarm| GA
    end
