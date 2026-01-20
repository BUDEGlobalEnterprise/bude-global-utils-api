from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.openapi.docs import get_swagger_ui_html
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.core.config import settings
from app.core.response import APIResponse
from app.tools.status import router as status_router
from app.tools.excuse import router as excuse_router
from app.tools.decision import router as decision_router
from app.tools.shrug import router as shrug_router
from app.tools.friday import router as friday_router
from app.tools.synergy import router as synergy_router
from app.tools.teapot import router as teapot_router
from app.tools.validate import router as validate_router

# Batch 1: Utils
from app.tools.uuid import router as uuid_router
from app.tools.time import router as time_router
from app.tools.base64 import router as base64_router
from app.tools.hash import router as hash_router
from app.tools.password import router as password_router
from app.tools.slug import router as slug_router
from app.tools.color import router as color_router

# Batch 2: Content
from app.tools.lorem import router as lorem_router
from app.tools.dadjoke import router as dadjoke_router
from app.tools.zen import router as zen_router
from app.tools.oblique import router as oblique_router
from app.tools.quote import router as quote_router
from app.tools.hello import router as hello_router
from app.tools.flip import router as flip_router

# Batch 3: Inspection
from app.tools.ip import router as ip_router
from app.tools.headers import router as headers_router
from app.tools.useragent import router as useragent_router
from app.tools.http import router as http_router
from app.tools.port import router as port_router
from app.tools.mime import router as mime_router
from app.tools.country import router as country_router

# Rate Limiter setup
limiter = Limiter(key_func=get_remote_address, default_limits=["120/minute"])

tags_metadata = [
    {"name": "Status", "description": "Operations to check system and service status."},
    {"name": "Excuse", "description": "Generate professional developer excuses."},
    {"name": "Decision", "description": "Tools for making important decisions properly."},
    {"name": "Shrug", "description": "The shrug emoji generator."},
    {"name": "Friday", "description": "Deployment safety advisor."},
    {"name": "Synergy", "description": "Corporate buzzword generator."},
    {"name": "Teapot", "description": "RFC 2324 implementation."},
    {"name": "Validate", "description": "Universal validation tool."},
    
    # Batch 1
    {"name": "UUID", "description": "UUID generation."},
    {"name": "Time", "description": "Time conversion and current time."},
    {"name": "Base64", "description": "Text encoding and decoding."},
    {"name": "Hash", "description": "SHA256 and MD5 hashing."},
    {"name": "Password", "description": "Secure password generation."},
    {"name": "Slug", "description": "URL-friendly slug generation."},
    {"name": "Color", "description": "Hex/RGB conversion."},

    # Batch 2
    {"name": "Lorem", "description": "Lorem Ipsum generator."},
    {"name": "Dadjoke", "description": "Random dad jokes."},
    {"name": "Zen", "description": "The Zen of Python."},
    {"name": "Oblique", "description": "Brian Eno's Oblique Strategies."},
    {"name": "Quote", "description": "Inspirational tech quotes."},
    {"name": "Hello", "description": "Hello World in various languages."},
    {"name": "Flip", "description": "Table flip text utils."},

    # Batch 3
    {"name": "IP", "description": "Client IP inspection."},
    {"name": "Headers", "description": "Request header inspection."},
    {"name": "UserAgent", "description": "User-Agent parsing."},
    {"name": "HTTP", "description": "HTTP status code descriptions."},
    {"name": "Port", "description": "Common port number lookup."},
    {"name": "Mime", "description": "MIME type lookup."},
    {"name": "Country", "description": "Country code lookup."},

    {"name": "Health", "description": "API health check."},
]

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_tags=tags_metadata,
    docs_url=None,
    redoc_url=None,
)

# Add Rate Limit State to app
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

# Register Routers
app.include_router(status_router.router, prefix="/status", tags=["Status"])
app.include_router(excuse_router.router, prefix="/excuse", tags=["Excuse"])
app.include_router(decision_router.router, prefix="/decision", tags=["Decision"])
app.include_router(shrug_router.router, prefix="/shrug", tags=["Shrug"])
app.include_router(friday_router.router, prefix="/friday", tags=["Friday"])
app.include_router(synergy_router.router, prefix="/synergy", tags=["Synergy"])
app.include_router(teapot_router.router, prefix="/brew", tags=["Teapot"])
app.include_router(validate_router.router, prefix="/validate", tags=["Validate"])

# Batch 1 Routes
app.include_router(uuid_router.router, prefix="/uuid", tags=["UUID"])
app.include_router(time_router.router, prefix="/time", tags=["Time"])
app.include_router(base64_router.router, prefix="/base64", tags=["Base64"])
app.include_router(hash_router.router, prefix="/hash", tags=["Hash"])
app.include_router(password_router.router, prefix="/password", tags=["Password"])
app.include_router(slug_router.router, prefix="/slug", tags=["Slug"])
app.include_router(color_router.router, prefix="/color", tags=["Color"])

# Batch 2 Routes
app.include_router(lorem_router.router, prefix="/lorem", tags=["Lorem"])
app.include_router(dadjoke_router.router, prefix="/dadjoke", tags=["Dadjoke"])
app.include_router(zen_router.router, prefix="/zen", tags=["Zen"])
app.include_router(oblique_router.router, prefix="/oblique", tags=["Oblique"])
app.include_router(quote_router.router, prefix="/quote", tags=["Quote"])
app.include_router(hello_router.router, prefix="/hello", tags=["Hello"])
app.include_router(flip_router.router, prefix="/flip", tags=["Flip"])

# Batch 3 Routes
app.include_router(ip_router.router, prefix="/ip", tags=["IP"])
app.include_router(headers_router.router, prefix="/headers", tags=["Headers"])
app.include_router(useragent_router.router, prefix="/useragent", tags=["UserAgent"])
app.include_router(http_router.router, prefix="/http", tags=["HTTP"])
app.include_router(port_router.router, prefix="/port", tags=["Port"])
app.include_router(mime_router.router, prefix="/mime", tags=["Mime"])
app.include_router(country_router.router, prefix="/country", tags=["Country"])



@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    response = get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
    )
    body = response.body.decode("utf-8")
    # Inject Vercel Speed Insights script
    script = """
    <script>
      window.si = window.si || function () { (window.siq = window.siq || []).push(arguments); };
    </script>
    <script defer src="/_vercel/speed-insights/script.js"></script>
    """
    return HTMLResponse(body.replace("</body>", script + "</body>"))




# Icon Mapping for Home Page
ICON_MAP = {
    "Status": "activity",
    "Excuse": "message-square-dashed",
    "Decision": "git-branch",
    "Shrug": "smile",
    "Friday": "calendar-off",
    "Synergy": "briefcase",
    "Teapot": "coffee",
    "Validate": "check-circle-2",
    "UUID": "fingerprint",
    "Time": "clock",
    "Base64": "binary",
    "Hash": "hash",
    "Password": "key",
    "Slug": "link",
    "Color": "palette",
    "Lorem": "align-left",
    "Dadjoke": "laugh",
    "Zen": "feather",
    "Oblique": "lightbulb",
    "Quote": "quote",
    "Hello": "globe-2",
    "Flip": "refresh-ccw",
    "IP": "network",
    "Headers": "list",
    "UserAgent": "monitor",
    "HTTP": "server",
    "Port": "anchor",
    "Mime": "file-code",
    "Country": "flag",
    "Health": "heart-pulse",
}


@app.get("/", tags=["Home"])
async def home_page():
    """
    **Home Page**
    Serves the HTML landing page with Speed Insights and Dynamic API Grid.
    """
    html_path = Path(__file__).parent / "home.html"
    content = html_path.read_text(encoding="utf-8")
    
    # API Grid Generation
    grid_html = ""
    
    # Endpoints that support simple GET requests without parameters
    TESTABLE_ENDPOINTS = {
        "Status": "/status",
        "Excuse": "/excuse",
        "Decision": "/decision",
        "Shrug": "/shrug",
        "Friday": "/friday",
        "Synergy": "/synergy",
        "Teapot": "/brew",
        "UUID": "/uuid",
        "Time": "/time",
        "Dadjoke": "/dadjoke",
        "Zen": "/zen",
        "Oblique": "/oblique",
        "Quote": "/quote",
        "Hello": "/hello",
        "Flip": "/flip",
        "IP": "/ip",
        "Headers": "/headers",
        "UserAgent": "/useragent",
        "HTTP": "/http", # Might need param, check defaults. Assuming defaults or just descriptive.
        "Country": "/country", # Likely needs param, will skip if unsure or check docs.
        "Lorem": "/lorem",
        "Color": "/color",
    }
    
    for tag in tags_metadata:
        name = tag["name"]
        if name == "Health": continue 
        
        description = tag["description"]
        icon = ICON_MAP.get(name, "box")
        
        # Determine if testable
        endpoint = TESTABLE_ENDPOINTS.get(name)
        
        action_html = ""
        if endpoint:
            # Render Quick Test Button
            action_html = f"""
            <div class="mt-auto pt-4 flex gap-2">
                <button id="btn-{name}" onclick="runQuickTest('{endpoint}', '{name}')" class="inline-flex items-center justify-center rounded-md text-xs font-medium bg-primary/10 text-primary hover:bg-primary/20 px-3 py-2 transition-colors">
                    <i data-lucide="play" class="mr-1.5 h-3 w-3"></i> Quick Test
                </button>
                <a href="/docs#/operations/{name}" class="inline-flex items-center justify-center rounded-md text-xs font-medium text-muted-foreground hover:text-foreground px-3 py-2 transition-colors">
                    Docs
                </a>
            </div>
            <pre id="result-{name}" class="hidden mt-3 p-3 bg-muted rounded-md text-xs font-mono overflow-auto max-h-40 whitespace-pre-wrap border border-border"></pre>
            """
        else:
             # Just Docs Link
             action_html = f"""
             <div class="mt-auto pt-4">
                <a href="/docs#/operations/{name}" class="inline-flex items-center justify-center rounded-md text-xs font-medium bg-secondary text-secondary-foreground hover:bg-secondary/80 px-3 py-2 transition-colors">
                    View Documentation <i data-lucide="arrow-right" class="ml-1.5 h-3 w-3"></i>
                </a>
             </div>
             """
        
        card = f"""
        <div class="group relative flex flex-col overflow-hidden rounded-xl border border-border bg-card p-6 shadow-sm transition-all duration-300 hover:shadow-md hover:border-primary/20">
            <div class="mb-4 inline-flex h-10 w-10 items-center justify-center rounded-lg bg-primary/5 text-primary">
                <i data-lucide="{icon}" class="h-5 w-5"></i>
            </div>
            <h3 class="text-lg font-bold text-foreground mb-2">{name}</h3>
            <p class="text-sm text-muted-foreground mb-4 line-clamp-2">{description}</p>
            {action_html}
        </div>
        """
        grid_html += card
        
    # Inject Grid
    final_html = content.replace("__API_GRID__", grid_html)
    return HTMLResponse(content=final_html)


@app.get("/api/health", tags=["Health"])
# Add rate limit to specific route if needed, or rely on default
@limiter.limit("120/minute") 
async def health_check(request: Request):
    """
    **System Health Check**
    
    Returns basic information about the API to verify it is running and operational.
    """
    return APIResponse.success(
        message="Bude Utils API is running",
        data={
            "app": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "status": "operational",
            "rate_limit": "120/minute per IP"
        }
    )
