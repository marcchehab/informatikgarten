import React, { useRef, useEffect } from "react";

import { MDXRemote } from "next-mdx-remote";
import { Mermaid, Pre } from "@portaljs/core";
import TurtleEditor from "./TurtleEditor";
import { Callout } from "@portaljs/remark-callouts";

import layouts from "@/layouts";
import { useTheme } from "next-themes";
import { ReactSVG } from "react-svg";

// Custom components/renderers to pass to MDX.
// Since the MDX files aren't loaded by webpack, they have no knowledge of how
// to handle import statements. Instead, you must include components in scope
// here.

function extractTextFromChildren(children: React.ReactNode): string {
    if (typeof children === "string") {
        return children;
    }

    if (Array.isArray(children)) {
        return children.map(extractTextFromChildren).join("");
    }

    if (
        React.isValidElement(children) &&
        (children as React.ReactElement).props.children
    ) {
        return extractTextFromChildren(
            (children as React.ReactElement).props.children
        );
    }

    return "";
}

const codeBlockWrapper = (props) => {
    let {children, className} = props;
    if (!className && children) {
        className = children.props.className;
    }
    if (className) {
        if (className.includes("language-turtle")) {
            return (
                <TurtleEditor className={className}>
                    {extractTextFromChildren(children)}
                </TurtleEditor>
            );
        }
        
        if (className.includes("language-codepen")) {
            const code = extractTextFromChildren(children);
            let codeSdx = [];
            for (const [index, part] of code.split("---").entries()) {
                if (!part.trim()) continue;
                const index = part.indexOf('\n');
                const lang = part.slice(0, index).trim();
                const content = part.slice(index + 1).trim();
                
                codeSdx.push(<pre key={index} data-lang={lang}>{content}</pre>)
            }
        
            const codepenWrapperRef = useRef(null);
        
            useEffect(() => {
                const script = document.createElement('script');
                script.src = "https://static.codepen.io/assets/embed/ei.js";
                script.async = true;
                document.body.appendChild(script);
        
                const handleFullscreenClick = () => {
                    if (document.fullscreenElement) {
                        document.exitFullscreen();
                    } else if (codepenWrapperRef.current.requestFullscreen) {
                        codepenWrapperRef.current.requestFullscreen();
                    } else if (codepenWrapperRef.current.mozRequestFullScreen) { /* Firefox */
                        codepenWrapperRef.current.mozRequestFullScreen();
                    } else if (codepenWrapperRef.current.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
                        codepenWrapperRef.current.webkitRequestFullscreen();
                    } else if (codepenWrapperRef.current.msRequestFullscreen) { /* IE/Edge */
                        codepenWrapperRef.current.msRequestFullscreen();
                    }
                };
        
                const fullscreenButton = document.createElement('button');
                fullscreenButton.innerText = 'Fullscreen';
                fullscreenButton.addEventListener('click', handleFullscreenClick);
                codepenWrapperRef.current.appendChild(fullscreenButton);
        
                return () => {
                    document.body.removeChild(script);
                    fullscreenButton.removeEventListener('click', handleFullscreenClick);
                }
            }, []);
        
            return <>
                <div ref={codepenWrapperRef} className="codepen-wrapper">
                    <div className="codepen" data-editable="true" data-prefill data-theme-id="1" data-default-tab="html,result">
                        {codeSdx}
                    </div>
                </div>
            </>
        }
    }

    // If we're here, it's a normal code block
    return <Pre className={className}>{children}</Pre>;
};

const Excalidraw = ({ alt, srcDark, srcLight }) => {
    const { theme } = useTheme();
    const src = theme === "dark" ? srcDark : srcLight;
    return <ReactSVG src={src} name={alt} />;
};

const components = {
    mermaid: Mermaid,
    pre: codeBlockWrapper,
    TurtleEditor: TurtleEditor,
    blockquote: Callout,
    Excalidraw: Excalidraw,
};

export default function MdxPage({ source, frontMatter }) {
    const Layout = ({ children }) => {
        if (frontMatter.layout) {
            const LayoutComponent = layouts[frontMatter.layout];
            return <LayoutComponent {...frontMatter}>{children}</LayoutComponent>;
        }
        return <>{children}</>;
    };

    return (
        <main id="mdxpage" className="prose max-w-none mx-auto">
            <Layout>
                <MDXRemote {...source} components={components} />
            </Layout>
        </main>
    );
}
