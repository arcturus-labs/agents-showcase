from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Company:
    name: str
    siteUrl: str
    size: str


@dataclass
class JobOpening:
    title: str
    seniorityLevel: str
    department: str
    subDepartments: list[str]
    jobDescription: str
    company: Company


@dataclass
class Application:
    id: str
    firstName: str
    lastName: str
    email: str
    mobile: str
    bio: str
    linkedinUrl: str
    region: str
    jobOpening: JobOpening


def example_application() -> Application:
    return Application(
        id="app-doug-turnbull-001",
        firstName="Doug",
        lastName="Turnbull",
        email="doug@example.com",
        mobile="+1-555-0101",
        bio=(
            "Search relevance engineer and educator focused on information retrieval, "
            "hybrid search, learning to rank, and LLM-powered search systems."
        ),
        linkedinUrl="https://www.linkedin.com/in/softwaredoug/",
        region="Charlottesville, Virginia, United States",
        jobOpening=JobOpening(
            title="Lead Mobile Product Designer",
            seniorityLevel="Lead",
            department="DESIGN",
            subDepartments=["PROD_MOBILE", "DES_UI"],
            jobDescription=(
                "We are hiring a lead mobile product designer to own end-to-end UX for our iOS and Android "
                "apps. The role requires strong product design craft, interaction design, prototyping, visual "
                "design systems experience, close partnership with product and engineering, and a portfolio "
                "showing shipped mobile consumer experiences."
            ),
            company=Company(
                name="Arcturus Labs",
                siteUrl="https://arcturuslabs.example.com",
                size="11-50",
            ),
        ),
    )
