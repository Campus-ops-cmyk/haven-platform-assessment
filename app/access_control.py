
from app.access_control import can_access_screening_report


def test_denies_access_to_another_landlords_report(
    property_managers, properties, tenants, screening_reports
):
    actor = next(pm for pm in property_managers if pm.id == "pm-001")
    report = next(r for r in screening_reports if r.id == "rep-002")

    result = can_access_screening_report(
        actor,
        report,
        properties=properties,
        tenants=tenants,
    )

    assert result is False


def test_allows_access_to_own_landlords_report(
    property_managers, properties, tenants, screening_reports
):
    actor = next(pm for pm in property_managers if pm.id == "pm-001")
    report = next(r for r in screening_reports if r.id == "rep-001")

    result = can_access_screening_report(
        actor,
        report,
        properties=properties,
        tenants=tenants,
    )

    assert result is True
