from django.contrib import admin
from calaccess import models
from .base import BaseAdmin


class CvrSoCdAdmin(BaseAdmin):
    pass


class Cvr2CampaignDisclosureCdAdmin(BaseAdmin):
    pass


class CvrCampaignDisclosureCdAdmin(BaseAdmin):
    pass


class DebtCdAdmin(BaseAdmin):
    pass


class ExpnCdAdmin(BaseAdmin):
    pass


class LoanCdAdmin(BaseAdmin):
    pass


class RcptCdAdmin(BaseAdmin):
    pass


class SpltCdAdmin(BaseAdmin):
    pass


class S496CdAdmin(BaseAdmin):
    pass


class S497CdAdmin(BaseAdmin):
    pass


class S498CdAdmin(BaseAdmin):
    pass


class S401CdAdmin(BaseAdmin):
    pass


class F501502CdAdmin(BaseAdmin):
    pass


admin.site.register(models.CvrSoCd, CvrSoAdmin)
admin.site.register(models.Cvr2SoCd, BaseAdmin)
admin.site.register(models.Cvr3VerificationInfoCd, BaseAdmin)
admin.site.register(
    models.CvrCampaignDisclosureCd,
    CvrCampaignDisclosureCdAdmin
)
admin.site.register(
    models.Cvr2CampaignDisclosureCd,
    Cvr2CampaignDisclosureCdAdmin
)
admin.site.register(models.DebtCd, DebtCdAdmin)
admin.site.register(models.ExpnCd, ExpnCdAdmin)
admin.site.register(models.F495P2Cd, BaseAdmin)
admin.site.register(models.LoanCd, LoanCdAdmin)
admin.site.register(models.RcptCd, RcptCdAdmin)
admin.site.register(models.SpltCd, SpltCdAdmin)
admin.site.register(models.S496Cd, S496CdAdmin)
admin.site.register(models.S497Cd, S497CdAdmin)
admin.site.register(models.S498Cd, S498CdAdmin)
admin.site.register(models.S401Cd, S401CdAdmin)
admin.site.register(models.F501502Cd, F501502CdAdmin)